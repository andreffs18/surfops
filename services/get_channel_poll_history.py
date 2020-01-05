import re
from surf import slack
from datetime import datetime
from cache import DummySlackCache
from models.message import MessageObject


class GetChannelPollHistoryService:
    """Returns last poll messages from given Slack Channel name and parses them into MessageObjects

    :param channel_name: Slack Channel name, without the "@"
    :type channel_name: string
    :returns: list of MessageObjects that represent "/poll" messages on Slack.
    :rtype: list
    """

    def __init__(self, channel_name, cache=None):
        self.cache = cache or DummySlackCache(slack)
        self.channel_id = self.cache.get_channel_id(channel_name)
        if not self.channel_id:
            raise ValueError('Slack channel "{}" not found.'.format(channel_name))

    def call(self):
        history = slack.channels.history(channel=self.channel_id)
        messages = filter(self._is_pool_message, history.body["messages"])
        return list(map(self._format_message, messages))

    @staticmethod
    def _is_pool_message(message):
        blocks = message.get("blocks", [])
        try:
            return all(
                [
                    message.get("subtype") == "bot_message",
                    len(blocks) == 4,
                    ":one:" in blocks[1]["text"]["text"],
                    ":two:" in blocks[2]["text"]["text"],
                ]
            )
        except Exception:
            return False

    def _get_usernames(self, message):
        users = re.findall(r"<@(.*?)>", message, re.DOTALL)
        return list(map(lambda user_id: self.cache.get_user_name(user_id), users))

    def _format_message(self, message):
        return MessageObject(
            title=message["text"],
            link=slack.chat.get_permalink(self.channel_id, message["ts"]).body[
                "permalink"
            ],
            timestamp=message["ts"],
            date=str(datetime.fromtimestamp(float(message["ts"])).date()),
            yes=",".join(self._get_usernames(message["blocks"][1]["text"]["text"])),
            no=",".join(self._get_usernames(message["blocks"][2]["text"]["text"])),
            count=len(self._get_usernames(message["blocks"][1]["text"]["text"])),
        )

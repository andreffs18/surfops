import re
from surf import slack, cache
from datetime import datetime
from models.message import MessageObject


class GetChannelPollHistory:
    """Returns last poll messages from given Slack Channel ID and parses them into MessageObjects

    :param channel_id: Slack Channel ID
    :type channel_id: string
    :returns: list of MessageObjects that represent "/poll" messages on Slack.
    :rtype: list
    """

    def __init__(self, channel_id):
        self.channel_id = channel_id

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

    @staticmethod
    def _get_usernames(message):
        users = re.findall(r"<@(.*?)>", message, re.DOTALL)
        return list(map(lambda user_id: cache.get_user_name(user_id), users))

    def _format_message(self, message):
        return MessageObject(
            title=message["text"],
            link=slack.chat.get_permalink(self.channel_id, message["ts"]).body["permalink"],
            timestamp=message["ts"],
            date=str(datetime.fromtimestamp(float(message["ts"])).date()),
            yes=",".join(self._get_usernames(message["blocks"][1]["text"]["text"])),
            no=",".join(self._get_usernames(message["blocks"][2]["text"]["text"])),
            count=len(self._get_usernames(message["blocks"][1]["text"]["text"]))
        )

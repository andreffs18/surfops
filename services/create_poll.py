from surf import slack
from cache import DummySlackCache


class CreatePollService:
    """Run "/poll" command on given Slack Channel with message from PoolObject.

    :param poll: PollObject that will be serialized and sent over
    :type poll: PoolObject
    :param channel_name: Slack Channel name to where the command "/poll" will be executed
    :type channel_name: string
    :returns: boolean representing if request was successful
    :rtype: bool
    """

    def __init__(self, poll, channel_name, cache=None):
        self.poll = poll
        self.cache = cache or DummySlackCache(slack)
        self.channel_id = self.cache.get_channel_id(channel_name)
        if not self.channel_id:
            raise ValueError('Slack channel "{}" not found.'.format(channel_name))

    def call(self):
        resp = slack.chat.command(
            channel=self.channel_id,
            command="/poll",
            text='"{}" "{}" "{}"'.format(
                self.poll.message, self.poll.yes, self.poll.no
            ),
        )
        return resp.error is None

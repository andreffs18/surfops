from surf import slack


class CreatePollService:
    """Run "/poll" command on given Slack Channel with message from PoolObject.

    :param poll: PollObject that will be serialized and sent over
    :type poll: PoolObject
    :param channel_id: Slack Channel ID to where the command "/poll" will be executed
    :type channel_id: string
    :returns: boolean representing if request was successful
    :rtype: bool
    """

    def __init__(self, poll, channel_id):
        self.poll = poll
        self.channel_id = channel_id

    def call(self):
        resp = slack.chat.command(
            channel=self.channel_id,
            command="/poll",
            text='"{}" "{}" "{}"'.format(
                self.poll.message, self.poll.yes, self.poll.no
            ),
        )
        return resp.error is None

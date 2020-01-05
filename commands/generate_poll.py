from surf import slack
from cache import DummySlackCache
from flask_script import Command, Option
from services.create_poll import CreatePollService
from services.poll_message_generator import PollMessageGeneratorService


class GeneratePollCommand(Command):

    option_list = [
        Option(
            "-c",
            "--channel",
            default="surfing",
            help="Slack Channel name to where /poll will be executed.",
            dest="channel_name",
        )
    ]

    def run(self, channel_name):
        poll = PollMessageGeneratorService().call()
        CreatePollService(poll, channel_name).call()
        print('Pool "{}" created with success!'.format(poll.message))

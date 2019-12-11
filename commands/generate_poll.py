from flask_script import Command, Option
from services.create_poll_service import CreatePollService
from services.poll_message_generator_service import PollMessageGeneratorService
from surf import cache


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
        channel_id = cache.get_channel_id(channel_name)
        if not channel_id:
            raise ValueError('Slack channel "{}" not found.'.format(channel_name))

        poll = PollMessageGeneratorService().call()
        CreatePollService(poll, channel_id).call()
        print('Pool "{}" created with success!'.format(poll.message))

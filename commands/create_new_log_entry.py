import os
import requests
from flask_script import Command, Option
from services.get_channel_poll_history import GetChannelPollHistoryService


class CreateNewLogEntryCommand(Command):
    option_list = [
        Option(
            "-c",
            "--channel",
            default="surfing",
            help="Slack Channel name to where /poll will be executed.",
            dest="channel_name",
        ),
        Option(
            "-h",
            "--hook",
            default=os.getenv("ZAPIER_CREATE_LOG_ENTRY_HOOK"),
            help="Zapier webhook to POST poll data.",
        ),
    ]

    def run(self, channel_name, hook):
        messages = GetChannelPollHistoryService(channel_name).call()
        if not messages:
            raise ValueError(
                'No poll messages found on slack channel "{}".'.format(channel_name)
            )

        payload = messages[0].to_json()
        response = requests.post(hook, json=payload)
        if not response.ok:
            raise response.raise_for_status()
        print(
            'New Entry was added to spreadsheet with date "{}"!'.format(
                payload.get("date")
            )
        )

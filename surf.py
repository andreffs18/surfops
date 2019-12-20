import os
from flask import Flask
from flask_script import Manager
from slacker import Slacker

manager = Manager(Flask(__name__))
slack = Slacker(os.getenv("SLACK_API_TOKEN"))

if __name__ == "__main__":
    from commands.generate_poll import GeneratePollCommand
    from commands.create_new_log_entry import CreateNewLogEntryCommand
    from commands.update_last_log_entry import UpdateLastLogEntryCommand

    manager.add_command("generate-poll", GeneratePollCommand)
    manager.add_command("create-new-log-entry", CreateNewLogEntryCommand)
    manager.add_command("update-last-log-entry", UpdateLastLogEntryCommand)
    manager.run()

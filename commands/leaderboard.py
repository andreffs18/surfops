from datetime import datetime
from flask_script import Command, Option
from services.get_surf_history_spreadsheet import GetSurfHistorySpreadsheetService
from services.count_surf_attendance import CountSurfAttendanceService
from services.pretty_print_leaderboard import PrettyPrintLeaderboardService


class LeaderboardCommand(Command):

    option_list = [
        Option(
            "-f",
            "--filepath",
            default="spreadsheet.tsv",
            help="Absolute location for spreadsheet file. Must be in the .tsv format.",
            dest="filepath",
        ),
        Option(
            "-pp",
            action='store_true',
            help="Pretty print leaderboard in a tabulated way.",
            dest="pretty_print",
        ),
        Option(
            "-l",
            "--limit",
            default=16,
            type=int,
            help="Maximum amount of people that we allow on the Surf Retreat.",
            dest="limit",
        ),
        Option(
            "-t",
            "--top",
            default=25,
            type=int,
            help="Limit leaderboard by \"top\" number.",
            dest="top",
        ),
        Option(
            "-s",
            "--start-date",
            required=False,
            default=datetime.min,
            dest="start_date",
            type=lambda d: datetime.strptime(d, "%Y-%m-%d"),
            help="From where should we start counting for the leaderboard. Format: YYYY-MM-DD. Time will be set to 00:00 utc",
        ),
        Option(
            "-e",
            "--end-date",
            required=False,
            default=datetime.max,
            dest="end_date",
            type=lambda d: datetime.strptime(d, "%Y-%m-%d"),
            help="From where should we stop counting for the leaderboard. Format: YYYY-MM-DD. Time will be set to 00:00 utc",
        ),
    ]

    def run(self, filepath, pretty_print, limit, top, start_date, end_date):
        spreadsheet = GetSurfHistorySpreadsheetService(filepath, start_date, end_date).call()
        leaderboard = CountSurfAttendanceService(spreadsheet).call()

        if pretty_print:
            PrettyPrintLeaderboardService(leaderboard, limit=limit, top=top).call()
        else:
            print(leaderboard)

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
        )
    ]

    def run(self, filepath, pretty_print, limit, top):
        spreadsheet = GetSurfHistorySpreadsheetService(filepath).call()
        leaderboard = CountSurfAttendanceService(spreadsheet).call()

        if pretty_print:
            PrettyPrintLeaderboardService(leaderboard, limit=limit, top=top).call()
        else:
            print(leaderboard)

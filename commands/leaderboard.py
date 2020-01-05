from flask_script import Command, Option
from services.get_surf_history_spreadsheet import GetSurfHistorySpreadsheetService
from services.count_surf_attendance import CountSurfAttendanceService
from services.pretty_print_leaderboard import PrettyPrintLeaderboardService


class LeaderboardCommand(Command):

    option_list = [
        Option(
            "-pp",
            action='store_true',
            help="Pretty print leaderboard in a tabulated way.",
            dest="pretty_print",
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

    def run(self, pretty_print, top):
        spreadsheet = GetSurfHistorySpreadsheetService().call()
        leaderboard = CountSurfAttendanceService(spreadsheet).call()

        if pretty_print:
            PrettyPrintLeaderboardService(leaderboard).call()
        else:
            print(leaderboard)

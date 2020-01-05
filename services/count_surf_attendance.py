class CountSurfAttendanceService:
    """From list of SpreadsheetRows objects, generate counter for all registered attendees on
    Surf History Spreadsheet and calculate score for each of them.

    :param rows: SpreadsheetRows that will be iterated over and build counter
    :type list: list of SpreadsheetRows
    :returns: dict of SpreadsheetRows that represent each row of the Surf History Spreadsheet
    :rtype: dict
    """

    def __init__(self, rows):
        self.rows = rows
        self.leaderboard = {}

    def call(self):
        for row in self.rows:

            for surfer in row.who_signup:
                self.leaderboard.setdefault(surfer, 0)

                if surfer in row.who_went:
                    self.leaderboard[surfer] += 1 * row.score

                if surfer in row.who_skipped:
                    self.leaderboard[surfer] -= 1 * row.score

        return self.leaderboard

from datetime import datetime
from models.spreadsheet_row import SpreadsheetRowObject


class GetSurfHistorySpreadsheetService:
    """Returns csv data from Surf History Spreadsheet that is fetched from given location.
    Each row should match the following format:
      [
        "Week",
        "Day Score",
        "Weather",
        "WhoSignUp?",
        "WhoWent?",
        "Number of Surfers",
        "Slack Pool Link"
      ]
    :param filepath: Location of Surf History Spreadsheet
    :type str: Absolute filepath for Spreadsheet file
    :param start_date: From which point in time should we start counting for the leaderboard
    :type datetime: datetime object
    :returns: list of RowObjects that represent each row of the Surf History Spreadsheet
    :rtype: list
    """

    def __init__(self, filepath, start_date, end_date):
        self.filepath = filepath
        self.start_date = start_date
        self.end_date = end_date

    def _get_spreadsheet_data(self):
        """
        Auxiliary method to parse given filepath into list of rows that map the spreadsheet
        """
        with open(self.filepath, "r+") as spreadsheet:
            # Ignore header
            spreadsheet = spreadsheet.readlines()[1:]

        parsed_spreadsheet = []
        for row in spreadsheet:
            row = row.split("\t")
            parsed_row = []
            for cell in row:
                cell = cell.strip()
                parsed_row.append(cell)
            parsed_spreadsheet.append(parsed_row)

        return parsed_spreadsheet

    def _in_between_dates(self, date):
        """
        Auxiliary method to check if given date (with format %Y-%m-%d) is between self.start_date and self.end_date.
        If no dates are given, we ignore then.
        """
        date = datetime.strptime(date, "%Y-%m-%d")
        return self.start_date < date < self.end_date

    def call(self):
        spreadsheet = self._get_spreadsheet_data()

        rows = []
        for date, score, description, who_signup, who_went, count, link in spreadsheet:

            if not self._in_between_dates(date):
                continue

            rows.append(SpreadsheetRowObject(date, score, description, who_signup, who_went, count, link))
        return rows

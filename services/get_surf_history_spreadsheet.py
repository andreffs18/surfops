from models.spreadsheet_row import SpreadsheetRowObject


class GetSurfHistorySpreadsheetService:
    """Returns csv data from Surf History Spreadsheet that is fetch from given location.
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
    :returns: list of RowObjects that represent each row of the Surf History Spreadsheet
    :rtype: list
    """

    def __init__(self, filepath):
        self.filepath = filepath

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

    def call(self):
        spreadsheet = self._get_spreadsheet_data()

        rows = []
        for datetime, score, description, who_signup, who_went, count, link in spreadsheet:
            rows.append(SpreadsheetRowObject(datetime, score, description, who_signup, who_went, count, link))
        return rows

from models.spreadsheet_row import SpreadsheetRowObject


class GetSurfHistorySpreadsheetService:
    """Returns csv data from Surf History Spreadsheet. Each row should match the following format:
    - [
        "Week",
        "Day Score",
        "Weather",
        "WhoSignUp?",
        "WhoWent?",
        "Number of Surfers",
        "Slack Pool Link"
    ]
    :returns: list of RowObjects that represent each row of the Surf History Spreadsheet
    :rtype: list
    """

    def __init__(self):
        pass

    def call(self):
        spreadsheet = [
            ["2020-01-01", "1", "Okay", "andre,filipe,ferreiro,da,silva", "andre,silva", "2", "http://andreffs.com"]
        ]

        rows = []
        for datetime, score, description, who_signup, who_went, count, link in spreadsheet:
            rows.append(
                SpreadsheetRowObject(datetime, score, description, who_signup, who_went, count, link)
            )
        return rows

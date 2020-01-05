from collections import Counter


class PrettyPrintLeaderboardService:
    """Print

    :param rows: SpreadsheetRows that will be iterated over and build counter
    :type list: list of SpreadsheetRows
    :returns: dict of SpreadsheetRows that represent each row of the Surf History Spreadsheet
    :rtype: dict
    """

    def __init__(self, leaderboard, limit=16, top=-1):
        self.leaderboard = leaderboard
        self.limit = limit
        self.top = top

    def call(self):
        print(u"| Going | Position | Surfer | Score |")
        print(u"| ----- | ----- | ----- | ----- |")
        for i, (surfer, score) in enumerate(Counter(self.leaderboard).most_common(), 1):
            if i > self.top:
                break
            if i <= self.limit:
                emoji = u"✅"
            else:
                emoji = u"❌"
            print(u"| {} | #{} | {} | {} |".format(emoji, i, surfer, score))

class SpreadsheetRowObject:
    """Surf History Spreadsheet row
    """

    def __init__(self, date, score, description, who_signup, who_went, total, link):
        self.date = date
        self.score = self._parse_to_int(score)
        self.description = description
        self.who_signup = self._clean_value(who_signup)
        self.who_went = self._clean_value(who_went)
        self.who_skipped = list(set(self.who_signup).difference(set(self.who_went)))
        self.total = total
        self.link = link

    def _parse_to_int(self, value):
        """Aux method to parse value to integer. If ValueError is raised, return zero instead

        :param value: String value to be parser to Integer
        :return: integer:
        """
        try:
            return int(value)
        except ValueError:
            return 0

    def _clean_value(self, value):
        """Aux method to clean string of name into separate string elements

        :param value: String of names. Eg: "jcortez,ricardo.rei,EduardoFFarah,"
        :return: list: Parsed string into list. Eg: ["jcortez", "ricardo.rei", "EduardoFFarah"]
        """
        return list(map(lambda v: v.strip(), value.split(",")))

    def to_json(self):
        return {
            "date": self.date,
            "score": self.score,
            "description": self.description,
            "who_signup": self.who_signup,
            "who_went": self.who_went,
            "who_skipped": self.who_skipped,
            "total": self.total,
            "link": self.link,
        }

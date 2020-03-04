class PollObject:
    """Poll slack object representation
    """

    def __init__(self, message, yes, no):
        self.message = message
        self.yes = yes
        self.no = no

    @property
    def text(self):
        """Return text of /poll command"""
        return '"{}" "{}" "{}"'.format(self.message, self.yes, self.no)
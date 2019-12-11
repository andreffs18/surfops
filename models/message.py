class MessageObject:
    """Message slack object representation
    """

    def __init__(self, title, link, timestamp, date, yes, no, count):
        self.title = title
        self.link = link
        self.timestamp = timestamp
        self.date = date
        self.yes = yes
        self.no = no
        self.count = count

    def to_json(self):
        return {
            "title": self.title,
            "link": self.link,
            "timestamp": self.timestamp,
            "date": self.date,
            "yes": self.yes,
            "no": self.no,
            "count": self.count,
        }

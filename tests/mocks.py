class MockSlackCache:
    def __init__(self):
        self.name = None

    def get_channel_id(self, channel_id):
        self.channel_id = channel_id
        return self.channel_id


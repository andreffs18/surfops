class DummySlackCache:
    """Dummy object to store necessary channels and users information from slack account

    :param slack: Slacker wrapper
    :type slack: Slacker object instance
    """
    CHANNELS = {}
    USERS = {}

    def __init__(self, slack):
        self.CHANNELS = self._set_channels_cache(slack)
        self.USERS = self._set_users_cache(slack)

    @staticmethod
    def _set_channels_cache(slack):
        r = slack.channels.list(exclude_archived=True)
        channels = dict(map(lambda channel: (channel["name"], channel["id"]), r.body["channels"]))
        print("> Got {} channels".format(len(channels)))
        return channels

    @staticmethod
    def _set_users_cache(slack):
        r = slack.users.list()
        users = dict(map(lambda user: (user["id"], user["name"]), r.body["members"]))
        print("> Got {} users".format(len(users)))
        return users

    def get_channel_id(self, channel_name):
        try:
            return self.CHANNELS[channel_name]
        except KeyError as e:
            print("> Error: {}. Available channels: {}".format(str(e), self.CHANNELS))

    def get_user_name(self, user_id):
        try:
            return self.USERS[user_id]
        except KeyError as e:
            print("> Error: {}. Available users: {}".format(str(e), self.USERS))

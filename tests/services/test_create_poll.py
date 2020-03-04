import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from models.poll import PollObject
from tests.mocks import MockSlackCache
from services.create_poll import CreatePollService


class CreatePollTestCase(unittest.TestCase):

    def setUp(self):
        self.poll = PollObject('My poll', "Yes", "No")
        self.channel = "channel"

    @patch('slacker.Chat.command')
    def test_service_success(self, mock_slack):
        """Ensure that service calls slack.chat.command with expected params and no error is returned"""
        mock_slack.return_value = MagicMock(error=None)
        success, _ = CreatePollService(self.poll, self.channel, MockSlackCache()).call()
        self.assertTrue(success)
        self.assertTrue(mock_slack.called)
        mock_slack.assert_called_with(channel=self.channel, command="/poll", text=self.poll.text)


if __name__ == '__main__':
    unittest.main()

import json
import unittest
from Jira import Jira


class CreateTicketTest(unittest.TestCase):

    def setUp(self):
        self.api_data = self.get_data('response.json')
        self.ticket = Jira()

    def get_data(self, name):
        with open('{0}'.format(name), 'r') as test_data:
            return json.load(test_data)


if __name__ == '__main__':
    unittest.main()
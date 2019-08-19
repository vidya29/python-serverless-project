import requests
import json
from requests.auth import HTTPBasicAuth
import utilities
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

jira_username = utilities.get_parameter("jira-user")
jira_password = utilities.get_parameter("jira-password")
project = utilities.get_parameter("jira-project-name")

# project = 'TEST'
#
#
# jira_username = 'vidya'
# jira_password = 'pass'

#jira_url = 'http://52.42.78.141:8080'
jira_url = 'http://localhost:5050'



class Jira():

    def __init__(self):
        super(Jira, self)

    def get_jira_auth(self):
        return HTTPBasicAuth(jira_username, jira_password)

    def exists(_self, record_id):
        try:
            search_ticket_url = "{0}/rest/api/2/search?jql=project={1}+and+text~'alert +for +{2}'".format(
                jira_url, project, record_id)
            request = requests.get(search_ticket_url,
                                   auth=_self.get_jira_auth())
            total_tickets = request.json()['total']
            if total_tickets > 0:
                logger.info('Ticket for this record already exists in JIRA:')
                logger.info(record_id)
                return True

            return False

        except Exception as e:
            logger.info('Failed to determine if ticket exists in JIRA')
            return True

    def create(self, summary, description, issuetype):
        json_values = {
            "fields": {
                "project": {"key": project},
                "summary": summary,
                "description": description,
                "issuetype": {"name": issuetype}
            }
        }
        try:
            headers = {'Content-Type': 'application/json'}
            create_ticket_url = '{0}/rest/api/2/issue/'.format(jira_url)
            logger.info('Creating Jira ticket with following input:')

            logger.info(json_values)

            request = requests.post(create_ticket_url, headers=headers,
                                    auth=self.get_jira_auth(),
                                    data=json.dumps(json_values))

            logger.info('Jira creation response:')
            logger.info(request.json)

        except Exception as e:
            logger.info('Error occurred while creating ticket:')
            logger.info(e)

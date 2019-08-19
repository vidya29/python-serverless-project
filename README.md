# python-serverless-project

Problem: 
Automate creation of JIRA tickets on any alert.

Solution:
Serverless lambda application that runs every 2 days to look up for a condition and creates a Jira ticket with summary, description and issueType.

Design:
Once the application is deployed, the zip file is available in S3. 
Use SSM to store configurations key/value pairs

Key Assumption:
Jira is hosted and is up and running

Useful commands:

1. To deploy the app:
serverless deploy

2. To invoke the function manually,
sls invoke -f jira

3. To view the logs on console:
sls logs -f jira

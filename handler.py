from Jira import Jira
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_jira_tickets(event, context):
    ticket = Jira()
    logger.info(event)

    """
    
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "af6d270c3bmsha010ee698d0f9bap1231d0jsnaa4f4c817c0f"
    }
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q": "london,uk"}

    response = requests.request("GET", url, headers=headers,
                                params=querystring)
    
    """

    res = {"cod": "200", "message": 0.0072, "cnt": 40, "list":
        [{"dt": 1566118800,
          "main": {"temp": 288.36, "temp_min": 288.36, "temp_max": 288.7,
                   "pressure": 1004.23, "sea_level": 1004.23,
                   "grnd_level": 999.22, "humidity": 78, "temp_kf": -0.34},
          "weather": [{"id": 500, "main": "Rain",
                       "description": "light rain", "icon": "10d"}],
          "clouds": {"all": 99}, "wind": {"speed": 4.8, "deg": 236.684},
          "rain": {"3h": 1.562}, "sys": {"pod": "d"},
          "dt_txt": "2019-08-18 09:00:00"},
         {"dt": 1566129600,
          "main": {"temp": 292.72, "temp_min": 292.72, "temp_max": 292.978,
                   "pressure": 1004.75, "sea_level": 1004.75,
                   "grnd_level": 999.63, "humidity": 51, "temp_kf": -0.26},
          "weather": [{"id": 500, "main": "Rain",
                       "description": "light rain", "icon": "10d"}],
          "clouds": {"all": 50}, "wind": {"speed": 6.9, "deg": 248.098},
          "rain": {"3h": 0.063}, "sys": {"pod": "d"},
          "dt_txt": "2019-08-18 12:00:00"},
         {"dt": 1566140400,
          "main": {"temp": 293.23, "temp_min": 293.23, "temp_max": 293.4,
                   "pressure": 1005.92, "sea_level": 1005.92,
                   "grnd_level": 1000.51, "humidity": 52, "temp_kf": -0.17},
          "weather": [{"id": 500, "main": "Rain",
                       "description": "light rain", "icon": "10d"}],
          "clouds": {"all": 50}, "wind": {"speed": 6.87, "deg": 250.52},
          "rain": {"3h": 0.188}, "sys": {"pod": "d"},
          "dt_txt": "2019-08-18 15:00:00"}
         ]}

    for result in res['list']:
        if result['main']['temp'] < 289.0 and result['weather'][0]['description'] != 'clear sky':
            summary = result['weather'][0]['description']
            id = result['weather'][0]['id']
            if not ticket.exists(id):
                logger.info("Preparing to create a Jira ticket ...")
                summary = 'Alert for ' + str(id) + ' ' + str(summary)
                description = 'Creating Jira ticket....'
                issuetype = 'Task'

                logger.info("Creating ticket .... ")
                jira_response = ticket.create(summary, description, issuetype)

                return jira_response

# create_tickets1()
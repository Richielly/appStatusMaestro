import json
import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini");

def mensage_slack(msg):
    webhook_url = config['default']["webhook_url"]
    slack_data = {'text': msg}
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'A requisição retornou um erro %s, a resposta é:\n%s'
            % (response.status_code, response.text))
    return "Maestro pode estar parado."
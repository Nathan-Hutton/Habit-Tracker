import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv('/Users/natha/PycharmProjects/info.env')
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = os.getenv('PIXELA_TOKEN')
USERNAME = os.getenv('PIXELA_USERNAME')
GRAPH_ID = 'graph1984kesey'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
graph_params = {
    "id": GRAPH_ID,
    'name': 'Programming_graph',
    'unit': 'days',
    'type': 'int',
    'color': 'ajisai'
}
date = datetime.now().strftime("%Y%m%d")
pixel_params = {
    'date': date,
    'quantity': '15'
}
update_params = {
    'quantity': '20'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)

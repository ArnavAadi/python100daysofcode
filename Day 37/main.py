import requests

username = "arnavaadi"
token = "hjagshdavsdgywg"
endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=endpoint, json=user_params)
print(response.text)

endpoint2 = f"{endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "mins",
    "type": "int",
    "color": "sora"
}

response2 = requests.post(url=endpoint2, json=graph_config)

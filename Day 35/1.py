import requests
from twilio.rest import Client

Api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC541da57839574f974185127df266e156"
auth_token = "0a5cce667aadf5f7d2df7810e0569bb5"

params = {
    'lat': 28.459497,
    'lon': 77.026634,
    "exclude": "current,minutely,daily",
    'appid': "c36dc31faacc8defd30107f5ecb14ec4",
}

response = requests.get(Api_endpoint, params=params)
response.raise_for_status()
data = response.json()["hourly"]
rain = False
for hour in range(12):
    hour = data[hour]
    code = hour["weather"][0]["id"]
    if code < 700:
        rain = True

if rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Bring Umbrella',
        from_='+18065830261',
        to='+919650658502'
    )
    print(message.status)

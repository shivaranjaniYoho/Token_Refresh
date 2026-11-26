
import requests
import time

BASE_URL = "http://127.0.0.1:8000"

CLIENT_ID = "my_client"
CLIENT_SECRET = "my_secret"

access_token = None


def mask_token(token):
    # Show only the first 6 characters
    return token[:6] + "****"


def get_token():

    global access_token

    response = requests.post(
        BASE_URL + "/token",
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
    )

    response.raise_for_status()

    access_token = response.json()["access_token"]

    print("New token received:", mask_token(access_token))

    return access_token


def call_api(url):

    global access_token

    # Get token if we do not have one
    if access_token is None:
        get_token()

    # Call the API
    response = requests.get(
        url,
        headers={
            "Authorization": "Bearer " + access_token
        }
    )

    # If token expired, get a new token
    if response.status_code == 401:

        print("Token expired! Getting a new token...")

        get_token()

        # Retry the request once
        response = requests.get(
            url,
            headers={
                "Authorization": "Bearer " + access_token
            }
        )

    response.raise_for_status()

    return response.json()


# Call API for more than 30 seconds
for i in range(8):

    print("\nRequest number:", i + 1)

    result = call_api(BASE_URL + "/data")

    print(result["message"])

    time.sleep(10)

import requests

def get_access_token(client_id: str, client_secret: str):
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    access_token = response.json()["access_token"]

    return access_token


def get_user_id(user_name: str, client_id: str, acces_token: str):
    params = {
        "login": user_name
    }

    headers = {
        "Authorization": f"Bearer {acces_token}",
        "Client-Id": client_id
    }

    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=headers)

    return response.json()["data"][0]['id']


def get_stream(user_id: int, client_id: str, acces_token: str):
    params = {
        "user_id": user_id
    }

    headers = {
        "Authorization": f"Bearer {acces_token}",
        "Client-Id": client_id
    }

    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=headers)
    data = response.json()["data"]

    return data[0]
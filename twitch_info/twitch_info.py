import requests


def get_access_token(client_id: str, client_secret: str) -> str:
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)


    if response.json() == {'status': 400, 'message': 'invalid client'} or  response.json() == {'status': 403, 'message': 'invalid client secret'}:
        raise InvalidClient(response.json()['message'])

    access_token = response.json()["access_token"]

    return access_token


def get_user_id(user_name: str, client_id: str, acces_token: str) -> int:
    params = {
        "login": user_name
    }

    headers = {
        "Authorization": f"Bearer {acces_token}",
        "Client-Id": client_id
    }

    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=headers)

    if len(response.json()['data']) == 0:
        raise InvalidUser("Invalid user")

    return response.json()["data"][0]['id']


def get_stream(user_id: int, client_id: str, acces_token: str) -> dict:
    params = {
        "user_id": user_id
    }

    headers = {
        "Authorization": f"Bearer {acces_token}",
        "Client-Id": client_id
    }

    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=headers)

    if response.json() == {'error': 'Unauthorized', 'status': 401, 'message': 'OAuth token is missing'} or response.json() == {'error': 'Unauthorized', 'status': 401, 'message': 'Invalid OAuth token'}:
        raise InvalidOAuthToken(response.json()['message'])

    if response.json() == {'error': 'Unauthorized', 'status': 401, 'message': 'Client ID and OAuth token do not match'}:
        raise ValuesNotMatching(response.json()['message']) 

    if response.json() == {'data': [], 'pagination': {}}:
        return "This user is not streaming"

    data = response.json()["data"]
    
    return data[0]

class InvalidUser(Exception):
    pass

class InvalidClient(Exception):
    pass

class InvalidOAuthToken(Exception):
    pass

class ValuesNotMatching(Exception):
    pass
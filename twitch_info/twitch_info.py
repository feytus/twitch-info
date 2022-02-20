import requests
from colorama import Fore

def get_user_id(user_name: str, acces_token: str, client_id: str):
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': client_id,
        'Authorization': 'OAuth ' + acces_token,
    }
    response = requests.get(
        'https://api.twitch.tv/kraken/users?login=' + user_name, headers=headers)
    data = response.json()
    if data == {'_total': 0, 'users': []}:
        return(Fore.YELLOW,
             f"{user_name} is not a twitch channel", Fore.RESET)
    return data["users"][0]["_id"]

def get_stream(user_id: int, headers: dict):
    response = requests.get(
        'https://api.twitch.tv/kraken/streams/' + user_id, headers=headers)
    data = response.json()
    if data == {'stream': None}:
        data_stream = {
            "on_stream": False
        }
    elif data == {'error': 'Bad Request', 'status': 400, 'message': 'The parameter "id" was malformed: the value must match the regular expression /^[0-9]+$/'}:
        exit({'error': 'Bad Request', 'status': 400,
             'message': 'The parameter "id" was malformed: the value must match the regular expression /^[0-9]+$/'})
    else:
        data_stream = {
            "on_stream": True,
            "display_name": data['stream']['channel']['display_name'],
            "logo": data['stream']['channel']['logo'],
            "game": data['stream']['game'],
            "viewer_count": data['stream']['viewers'],
            "preview_image": data['stream']['preview']['large'],
            "title": data['stream']['channel']['status'],
            "date": data['stream']['created_at'],
        }
    return data_stream
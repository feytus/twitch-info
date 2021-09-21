import requests
from colorama import Fore
from datetime import datetime
import random


def get_color(color1, color2, color3):
    rand_numb = random.randint(1, 3)
    if rand_numb == 1:
        return color1
    elif rand_numb == 2:
        return color2
    elif rand_numb == 3:
        return color3


class twitch_info:
    """
    # Twitch informations.
    ### Github link

    https://github.com/feytus/twitch-info
    """

    def __init__(self, client_id: str, acces_token: str):
        self.client_id = client_id
        self.acces_token = acces_token

    def get_user_id(self, user_name: str):
        self.headers = {
            'Accept': 'application/vnd.twitchtv.v5+json',
            'Client-ID': self.client_id,
            'Authorization': 'OAuth ' + self.acces_token,
        }
        response = requests.get(
            'https://api.twitch.tv/kraken/users?login=' + user_name, headers=self.headers)
        data = response.json()
        if data == {'_total': 0, 'users': []}:
            return(Fore.YELLOW,
                 f"{user_name} is not a twitch channel", Fore.RESET)

        return data["users"][0]["_id"]

    def get_stream(self, user_id: int):
        response = requests.get(
            'https://api.twitch.tv/kraken/streams/' + user_id, headers=self.headers)
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

    def check_for_stream(self, user: str, *, webhook_url: str = None):
        full_date = datetime.now()
        date = full_date.strftime('%Y-%m-%d-%H-%M-%S')
        data_stream = self.get_stream(user_id=self.get_user_id(user))
        if data_stream['on_stream'] == True:  # if user is streaming
            # Send embed to discord using webhooks
            if webhook_url != None:
                data = {
                    "username": "Twitch Feeder",
                    "avatar_url": "https://i.imgur.com/EmfpNrz.png",
                    "embeds": [
                        {
                            "title": data_stream['title'],
                            "url": "https://twitch.tv/" + data_stream['display_name'],
                            "color": get_color(0xac05ff, 0x8e05ff, 0x05b4ff),
                            "fields": [
                                {
                                    "name": "Game",
                                    "value": data_stream['game'],
                                    "inline": True
                                },
                                {
                                    "name": "Viewer count",
                                    "value": data_stream['viewer_count'],
                                    "inline": True
                                }
                            ],
                            "author": {
                                "name": data_stream['display_name'],
                                "url": "https://twitch.tv/" + data_stream['display_name'],
                                "icon_url": data_stream['logo']
                            },
                            "footer": {
                                "text": "Twitch"
                            },
                            "timestamp": data_stream['date'],
                            "image": {
                                "url": data_stream['preview_image']
                            },
                            "thumbnail": {
                                "url": "https://static-cdn.jtvnw.net/ttv-boxart/" + data_stream['game'].replace(" ", "%20") + ".jpg"
                            }
                        }
                    ]
                }
                try:
                    result = requests.post(
                        url=webhook_url, json=data)
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                    
                return data_stream

        return data_stream

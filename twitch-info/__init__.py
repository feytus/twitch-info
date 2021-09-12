import requests
import time
from colorama import Fore
import logging
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
        self.data = response.json()
        if self.data == {'_total': 0, 'users': []}:
            exit(f"{user_name} is not a twitch channel")

        return self.data["users"][0]["_id"]

    def get_stream(self, user_id: int):
        response = requests.get(
            'https://api.twitch.tv/kraken/streams/' + user_id, headers=self.headers)
        self.data = response.json()
        if self.data == {'stream': None}:
            self.data_stream = {
                "on_stream": False
            }
        elif self.data == {'error': 'Bad Request', 'status': 400, 'message': 'The parameter "id" was malformed: the value must match the regular expression /^[0-9]+$/'}:
            exit({'error': 'Bad Request', 'status': 400,
                 'message': 'The parameter "id" was malformed: the value must match the regular expression /^[0-9]+$/'})
        else:
            self.data_stream = {
                "on_stream": True,
                "display_name": self.data['stream']['channel']['display_name'],
                "logo": self.data['stream']['channel']['logo'],
                "game": self.data['stream']['game'],
                "viewer_count": self.data['stream']['viewers'],
                "preview_image": self.data['stream']['preview']['large'],
                "title": self.data['stream']['channel']['status'],
                "date": self.data['stream']['created_at'],
            }
        return self.data_stream

    def check_for_stream(self, user: str, *, webhook_url: str = None):
        first_time_1 = True

        full_date = datetime.now()
        date = full_date.strftime('%Y-%m-%d-%H-%M-%S')
        data_stream = self.get_stream(user_id=self.get_user_id(user))
        if data_stream['on_stream'] == True:  # if user is streaming
            logging.info(data_stream['display_name'] + ' is streaming')
            print(Fore.GREEN + date + " " +
                  data_stream['display_name'] + ' is streaming' + Fore.RESET)
            # Send embed to discord using webhooks
            if first_time_1 is True and webhook_url != None:
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
                                "url": "https://twitch.tv/" + self.data_stream['display_name'],
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
                first_time_1 = False
        # if user is not streaming
        elif data_stream['on_stream'] is False:
            try:
                logging.info(user + " is not streaming")
                print(Fore.RED + date + " " + user +
                      ' is not streaming' + Fore.RESET)
                first_time_1 = True
            except KeyError:
                pass

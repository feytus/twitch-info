# Twitch Informations

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/feytus/twitch-info?style=for-the-badge&logo=appveyor)
[![License](https://img.shields.io/github/license/feytus/twitch-info?style=for-the-badge)](https://github.com/feytus/twitch-info/blob/master/LICENSE)

Get informations about a **streamer** from **twitch.tv** and get **notified on discord**.

## Install the package

``pip install twitch-info``

## Exemple

```python
from twitch_info import get_user_id, get_stream

acces_token  = "<ACCES TOKEN>"
client_id = "<CLIENT ID>"
headers =  {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': client_id,
        'Authorization': 'OAuth ' + acces_token,
    }

user_id: int = get_user_id("<CHANNEL NAME>", acces_token, client_id)

user_info: dict = get_stream(user_id, headers)
```
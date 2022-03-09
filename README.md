# Twitch Informations

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/feytus/twitch-info?style=for-the-badge&logo=appveyor)
[![License](https://img.shields.io/github/license/feytus/twitch-info?style=for-the-badge)](https://github.com/feytus/twitch-info/blob/master/LICENSE)

Get informations about a **streamer** from **twitch.tv**.

## Install the package

``pip install twitch-info``

## Exemple

```python
from twitch_info import get_user_id, get_stream, get_access_token

# To get client_id and client_secret -> https://youtu.be/JK06TumS6ho

client_id = "<CLIENT ID>"
client_secret = "<CLIENT SECRET>" 


acces_token = get_access_token(client_id=client_id, client_secret=client_secret)

user_id = get_user_id(user_name="<CHANNEL_NAME>", client_id=client_id, acces_token=acces_token)

stream = get_stream(user_id=user_id, client_id=client_id, acces_token=acces_token)
```
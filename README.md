# Twitch Informations

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/feytus/twitch-info?style=for-the-badge&logo=appveyor)
[![License](https://img.shields.io/github/license/feytus/twitch-info?style=for-the-badge)](https://github.com/feytus/twitch-info/blob/master/LICENSE)

Get informations about a **streamer** from **twitch.tv** and get **notified on discord**.

## Install the package

``pip install twitch-info``

## Exemple

```python
from __init__ import twitch_info

twitch = twitch_info(client_id="<YOUR CLIENT ID>", 
                    acces_token="<YOUR CLIENT ID>")

user_id: int = twitch.get_user_id(user_name="<CHANNEL NAME>")

user_info: dict = twitch.get_stream(user_id=user_id)

is_in_live: bool = twitch.check_for_stream(user="<CHANNEL NAME>")
```

### Get user id

**Argument:**

- **user_name**: ***str***

**Return : *Int***

``213122``

### Check for stream

**Arguments:**

- **user**: ***str***
- **webhook_url**: ***str = None***

**Return : *Bool***

``True`` or ``False``

### Get stream

**Argument:**

- **user_id**: ***int***

**Return : *Dict***

```python
{
    "on_stream": True,
    "display_name": "TheGuill84",
    "logo": "https: //static-cdn.jtvnw.net/jtv_user_pictures/4e97c3fa121d46d3-profile_image-300x300.png",
    "game": "Mario Kart 8",
    "viewer_count": 1361,
    "preview_image": "https://static-cdn.jtvnw.net/previews-ttv/live_user_theguill84-640x360.jpg",
    "title": "GUILL ► TOP 1 TOURNOI DE PONCE AUJOURD'HUI (non) + plein d'UHC ! - !planning !subgoal !scenario",
    "date": "2021-09-12T12:45:16Z"
}
```

### Message on discord

![Image Discord Embed](https://i.imgur.com/Kd6Spvj.png)

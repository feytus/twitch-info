from __init__ import twitch_info

twitch = twitch_info(client_id="<YOUR CLIENT ID>", 
                    acces_token="<YOUR CLIENT ID>")

user_id: int = twitch.get_user_id(user_name="<CHANNEL NAME>")

user_info: dict = twitch.get_stream(user_id=user_id)

is_in_live: bool = twitch.check_for_stream(user="<CHANNEL NAME>")


from __init__ import twitch_info

twitch = twitch_info(client_id="<YOUR CLIENT ID>", 
                    acces_token="<YOUR CLIENT ID>")

user_id = twitch.get_user_id(user_name="<CHANNEL NAME>")

user_info = twitch.get_stream(user_id=user_id)

checking = twitch.check_for_stream(user="daiko")


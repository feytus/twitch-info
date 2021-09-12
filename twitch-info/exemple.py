from __init__ import twitch_info

twitch = twitch_info(client_id="<YOUR CLIENT ID>", 
                    acces_token="<YOUR CLIENT ID>")

twitch = twitch_info(client_id="0jmzb9j0q0rdpu7354p99x86b9e0me", 
                    acces_token="ui89bcrn9di0ed7ph0x1r8gd0dlqi7")

user_id = twitch.get_user_id(user_name="<CHANNEL NAME>")

user_info = twitch.get_stream(user_id=user_id)

checking = twitch.check_for_stream(user="daiko")


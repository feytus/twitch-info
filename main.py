from itertools import starmap
from twitch_info import get_user_id, get_stream, get_access_token

# To get client_id and client_secret -> https://youtu.be/JK06TumS6ho

client_secret="cflrb2w1bhzr3fhu0adc7lf5zwgbh1"
client_id="x6qs7a5tfnmjizt7fpjbb1z8ix433h"

acces_token = get_access_token(client_id=client_id, client_secret=client_secret)

user_id = get_user_id(user_name="otplol_", client_id=client_id, acces_token=acces_token)

stream = get_stream(user_id=user_id, client_id=client_id, acces_token=acces_token)

print(stream)
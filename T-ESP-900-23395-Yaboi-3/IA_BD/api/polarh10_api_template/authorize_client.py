import requests
import webbrowser
from utils import load_config, save_config
from accesslink import AccessLink

CONFIG_FILENAME = "config.yml"
config = load_config(CONFIG_FILENAME)
accesslink = AccessLink(client_id=config['client_id'],
                        client_secret=config['client_secret'])


webbrowser.open('https://flow.polar.com/oauth2/authorization?response_type=code&client_id=9fa6e5fc-ed8a-4473-a0a8-3bc01eb2de94')

print("Enter authorization code: ")
authorization_code = input()

token_response = accesslink.get_access_token(authorization_code)

config["user_id"] = token_response["x_user_id"]
config["access_token"] = token_response["access_token"]
save_config(config, CONFIG_FILENAME)


try:
    accesslink.users.register(access_token=config["access_token"])
except requests.exceptions.HTTPError as err:
    if err.response.status_code != 409:
        raise err

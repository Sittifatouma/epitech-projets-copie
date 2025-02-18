# coding: utf-8

import toml

import requests
from requests.auth import HTTPBasicAuth

config = toml.load("api.toml")

URL_TOKEN = config["url"]["TOKEN"]

CLIENT_ID = config["user"]["CLIENT_ID"]
CLIENT_SECRET = config["user"]["CLIENT_SECRET"]
CODE = config["user"]["CODE"]

def get_token():
    token_endpoint = requests.post(
        url=URL_TOKEN,
        data={
            "grant_type": "authorization_code",
            "code": CODE
        },
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    )

    return token_endpoint.json()
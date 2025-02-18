# coding: utf-8

import toml

import requests

config = toml.load("api.toml")

URL_REGISTER_USER = config["url"]["REGISTER_USER"]

TOKEN = config["user"]["TOKEN"]
AUTH = "Bearer " + TOKEN

ID = config["user"]["ID"]

def create_user_id():
    request = requests.post(
        url=URL_REGISTER_USER,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        },
        data={
            "member_id": ID
        }
    )
    
    return request.json()

def get_user_info():
    url = URL_REGISTER_USER + "/" + ID
    request = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        },
        data={
            "member_id": id
        }
    )
    
    return request.json()
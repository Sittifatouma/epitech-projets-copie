# coding: utf-8

import toml

import requests

config = toml.load("api.toml")

URL_CREATE_TRANSACTION = config["url"]["CREATE_TRANSACTION"]
URL_PHYSICAL_INFO = config["url"]["PHYSICAL_INFO"]

TOKEN = config["user"]["TOKEN"]
AUTH = "Bearer " + TOKEN

ID = config["user"]["ID"]
ID_TRANSACTION = config["transaction"]["ID"]
ID_PHYSICAL_INFO = config["physical-info"]["ID"]

def create_transaction():
    url = URL_CREATE_TRANSACTION.replace("<user_id>", ID)
    
    request = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        },
        data={
            "user_id": ID
        }
    )
    
    return request.json()

def list_physical_info():
    url = URL_CREATE_TRANSACTION.replace("<user_id>", ID) + "/" + ID_TRANSACTION
    
    # List physical info
    request_physical_info = requests.get(
        url=url,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        }
    )
    
    # Commit transaction
    request_commit_transaction = requests.put(
        url=url,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        }
    )
    
    assert request_commit_transaction.status_code == 200
    
    return request_physical_info.json()

def get_physical_info():
    url = URL_PHYSICAL_INFO.replace("<user_id>", ID).replace("<transaction-id>", ID_TRANSACTION) + "/" + ID_PHYSICAL_INFO
    
    request = requests.get(
        url=url,
        headers={
            'Content-Type': 'application/xml', 
            'Accept': 'application/json', 
            'Authorization': AUTH
        }
    )
    
    return request.json()
from django.http import JsonResponse
from rest_framework.decorators import api_view

import toml
import json

from .scripts import Requests_Authentication, Requests_User

# https://flow.polar.com/oauth2/authorization?response_type=code&client_id=9fa6e5fc-ed8a-4473-a0a8-3bc01eb2de94

@api_view(['GET'])
def home(request):
    return JsonResponse({"message": "Welcome to the prediction app :)"})

@api_view(['GET'])
def receive_code(request):
    api_config = toml.load("api.toml")
    
    code = request.GET.get("code")
    
    api_config["user"]["CODE"] = code
    
    with open("api.toml", 'w') as file:
        toml.dump(api_config, file)
    
    return JsonResponse({
        "message": "J'aime les endives"
    })

@api_view(['GET'])
def get_token(request):
    api_config = toml.load("api.toml")
    
    token_response = Requests_Authentication.get_token()
    print(token_response)
    
    token = token_response["access_token"]
    print(token)
    
    api_config["user"]["TOKEN"] = token
    
    with open("api.toml", 'w') as file:
        toml.dump(api_config, file)

    return JsonResponse({
        "message": "poyoo"
    })

@api_view(['GET'])
def register_user(request):   
    registration = Requests_User.create_user_id()
    
    print(registration)
    
    infos = Requests_User.get_user_info()
    
    print(infos)
    
    return JsonResponse({
        "message": "Registration done"
    })

@api_view(["GET"])
def transaction_user(request):
    return JsonResponse(
        {"message": "Transaction done"}
    )

@api_view(['POST'])
def predict(request):
    request = request.body
    if isinstance(request, bytes):
        request = request.decode('utf-8')
    
    request = json.loads(request)
    
    return JsonResponse({
        "message": request
    })

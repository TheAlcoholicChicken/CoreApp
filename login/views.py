import json
import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UsersCollection
from . import forms as F

# Global Constants
__TOKEN = 'fAAPH9QRF4AAvGn870kTJaKGKsMcNRBtfWZr7zOj4qQ'
__LOGIN_URL = 'https://management-system-api.herokuapp.com/user/login/'
__BADGE_URL = 'https://management-system-api.herokuapp.com/user/get_badges/'
__CREATE_ACCOUNT_URL = 'https://management-system-api.herokuapp.com/user/create_account'


# Create your views here.
# returns login page for http get requests
def login_page(request):
    return render(request, 'login.html')


# returns profile page for http get requests
def profile_page(request):
    return render(request, 'profile.html')


# returns landing page for http get requests
def landing_page(request):
    return render(request, 'index.html')


@csrf_exempt
def login(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('login|request.body:', data)
        response = requests.post(__LOGIN_URL,
                                 data={'user_email': data['email'],
                                       'password': data['password'],
                                       'token': __TOKEN})
        if response.status_code == 400:
            return JsonResponse({'msg': response.json()['msg']})
        elif response.status_code == 200 and response.json()['user_id'] != '':
            print('login|response.json()', response.json()['user_id'])
            msg = response.json()['msg']
            user_id = response.json()['user_id']
            url = 'user/' + user_id
            return JsonResponse({'msg': msg, 'user_id': user_id, 'url': url})
        else:
            msg = 'Management API not up or no response'
            print('login|', msg)
            return JsonResponse({'msg': msg})
    else:
        return JsonResponse({'response': 'Not a post request'})


#TODO implement try catch to clear errors when directed to user/
@csrf_exempt
def getUser(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('getUser|request.body:', data)
        userid = data['user_id']
        print('getUser|user_id', userid)
        result = UsersCollection.get_user_json(userid)
        if not result:
            return JsonResponse({'error': 'User does not exist'})
        return JsonResponse(result)
    else:
        return JsonResponse({'response': 'invalid form'})

@csrf_exempt
def searchUser(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('searchUser|request.body:', data)
        id = data['id_only'] if 'id_only' in data else True
        result = UsersCollection.search_user(data['search'], id)
        if result['users'] == []:
            return JsonResponse({'response': 'no users'})
        else:
            print(result)
            return JsonResponse({'response': 'users found', 'users': result['users']})
    else:
        return JsonResponse({'response': 'invalid form'})


@csrf_exempt
def getUserBadges(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        userid = data['user_id']
        print('getUserBadges|user_id', userid)
        response = requests.post(__BADGE_URL, data={'user_id': userid, 'token': __TOKEN})
        print('getUserBadges|response.json()', response.json())
        return JsonResponse(response.json())
    else:
        return JsonResponse({'response': 'invalid form'})


@csrf_exempt
def updateAccount(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('updateAccount|request.body:', data)
        result, updated = UsersCollection.set_user(data)
        return JsonResponse(
            {'response': result, 'message': 'User row index (Debugging)', 'update': updated})
    else:
        return JsonResponse({'response': 'invalid form'})


@csrf_exempt
def createAccount(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('createAccount|request.body:', data)
        # First check Management DB does not contain user:
        response = requests.post(__CREATE_ACCOUNT_URL,
                                 data={'user_email': data['email'],
                                       'password': data['password'],
                                       'token': __TOKEN})
        if response.status_code == 400:
            return JsonResponse({'msg': response.json()['msg']})
        elif response.status_code == 200 and response.json()['user_id'] != '':
            print('createAccount|response.json()', response.json()['user_id'])
            msg = response.json()['msg']
            user_id = response.json()['user_id']
            if UsersCollection.get_user_json(user_id) != False:
                print('createAccount|UC.get_user_json()', UsersCollection.get_user_json(user_id))
                return JsonResponse({'msg': 'Something bad happen'}, status=403)
            info = {"user_id": user_id,
                    "user_profile_link": "user/" + user_id,
                    "data": {
                        "first_name": data['email'],
                        "last_name": data['password'],
                        "profile_picture_url": "https://imgur.com/gallery/hUbESvH",
                        "description": ""
                    }}
            index, create = UsersCollection.set_user(info)
            return JsonResponse({'msg': msg, 'user_id': user_id, 'create': not create})
        else:
            msg = 'Management API not up or no response'
            print('createAccount|', msg)
            return JsonResponse({'msg': msg})
    else:
        return JsonResponse({'response': 'Not a post request'})
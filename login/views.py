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
        form = F.LoginUserForm(request.POST)
        if form.is_valid():
            print('login|form.cleaned_data', form.cleaned_data)
            form = form.cleaned_data
            response = requests.post(__LOGIN_URL,
                                     data={'user_email': form['email'],
                                           'password': form['password'],
                                           'token': __TOKEN})
            if response.status_code == 400:
                return JsonResponse({'response': response.json()['msg']})
            elif response.status_code == 200 and response.json()['user_id'] != '':
                print('login|response.json()', response.json()['user_id'])
                msg = response.json()['msg']
                user_id = response.json()['user_id']
                url = 'user/' + user_id
                return JsonResponse({'response': msg, 'user_id': user_id, 'url': url})
            else:
                msg = 'Management API not up or no response'
                print('login|', msg)
                return JsonResponse({'response': msg})
        else:
            return JsonResponse({'response': 'invalid form'})
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
        return JsonResponse(UsersCollection.get_user_json(userid))
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
        print('createAccount|request.body:', data)
        result, updated = UsersCollection.set_user(data)
        return JsonResponse(
            {'response': result, 'message': 'User row index (Debugging)', 'update': updated})
    else:
        return JsonResponse({'response': 'invalid form'})

#TODO Send create account to Management API
@csrf_exempt
def createAccount(request):
    return JsonResponse({'response': 'To be inplemented'})
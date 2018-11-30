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
def index(request):
    # TODO: render login.html
    return render(request, 'index.html')

#TODO Implement login request and response
@csrf_exempt
def login(request):
    print(str(request.path))
    return render(request, 'index.html')
    if request.method == 'POST':
        form = F.LoginUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            response = requests.post(__LOGIN_URL,
                                     data={'user_email': form.user_email,
                                           'password': form.password,
                                           'token': __TOKEN})
            if response.json()['success'] == 'True':  # if success, redirect to landing page
                return render(request, 'index.html')
            else:
                return JsonResponse({'response': response.json()['success']})


@csrf_exempt
def getUser(request):
    print(str(request.path))
    if request.method == 'GET':
        userid = request.path.split('/')[-1]
        print('getUser|user_id', userid)
        return JsonResponse(UsersCollection.get_user_json(userid))
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('getUser|request.body:', data)
        result = '\n'.join(UsersCollection.search_user(data['search']))
        if result == '':
            return JsonResponse({'response': 'no users'})
        else:
            print(result)
            return JsonResponse({'response': result})
    else:
        return JsonResponse({'response': 'invalid form'})


@csrf_exempt
def getUserBadges(request):
    print(str(request.path))
    if request.method == 'GET':
        userid = request.path.split('/')[-3]
        print('getUserBadges|',userid)
        response = requests.post(__BADGE_URL, data={'user_id':userid,'token':__TOKEN})
        print('getUserBadges|response.json()',response.json())
        return JsonResponse(response.json())
    return JsonResponse({'response': 'Not implemented'})


@csrf_exempt
def createAccount(request):
    print(str(request.path))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('createAccount|request.body:', data)
        result, updated = UsersCollection.set_user(data)
        return JsonResponse(
            {'response': result, 'message': 'User row index (Debugging)', 'update': updated})
    else:
        return JsonResponse({'response': 'invalid form'})

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
    return render(request, 'landing.html')


#TODO Implement login request and response
@csrf_exempt
def login(request):
    print(str(request.path))
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = F.LoginUserForm(request.POST)
        if form.is_valid():
            print('login|form.cleaned_data',form.cleaned_data)
            form = form.cleaned_data
            response = requests.post(__LOGIN_URL,
                                     data={'user_email': form['email'],
                                           'password': form['password'],
                                           'token': __TOKEN})
            if response.status_code == 400:
                return JsonResponse({'response': response.json()['msg']})
            else:
                print('login|response.json()', response.json()['user_id'])
                return render(request, 'index.html')
        else:
            return JsonResponse({'response': 'invalid form'})
    else:
        return JsonResponse({'response': 'Not a post request'})


#TODO implement try catch to clear errors when directed to user/
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


#TODO try catch block incase maanagement goes offline
@csrf_exempt
def getUserBadges(request):
    print(str(request.path))
    if request.method == 'GET':
        userid = request.path.split('/')[-3]
        print('getUserBadges|',userid)
        try:
            response = requests.post(__BADGE_URL, data={'user_id':userid,'token':__TOKEN})
            print('getUserBadges|response.json()',response.json())
            return JsonResponse(response.json())
        except:
            return JsonResponse({'response': 'Not implemented'})
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

import json
import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UsersCollection
from . import forms as F

# Global Constants
__TOKEN = 'G5NIJdnKD7CyuPsy1zi4euipxnNhc0WJwGd8qJHS4XA'
__LOGIN_URL = 'https://management-system-api.herokuapp.com/'

# Create your views here.
def index(request):
    #TODO: render login.html
    return render(request, 'index.html')


@csrf_exempt
def api(request):
    print(str(request.path))
    if request.method == 'POST':
        form = F.SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            search = form.cleaned_data.get('search')
            result = '\n'.join(UsersCollection.search_user(search))
            if result == '':
                return JsonResponse({'response': 'no users'})
            else:
                print(result)
                return JsonResponse({'response': result})
        else:
            return JsonResponse({'response': 'invalid form'})

@csrf_exempt
def login(request):
    print(str(request.path))
    if requests.method == 'POST':
        form = F.LoginUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            response = requests.post(__LOGIN_URL,
                                    body={'user_email': form.user_email,
                                          'password': form.password,
                                          'token': __TOKEN})
            if response.json()['success'] == 'True':
                return render(request, 'index.html')
            else:
                return JsonResponse({'response' : response.json()['success']})

@csrf_exempt
def createAccount(request):
    print(str(request.path))
    if request.method == 'POST':
        form = F.AddUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            userid = form.cleaned_data.get('userid')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            result = UsersCollection.set_user(userid, firstname, lastname)
            return JsonResponse({'response': result})
        else:
            return JsonResponse({'response': 'invalid form'})
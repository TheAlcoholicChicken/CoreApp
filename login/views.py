import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UsersCollection
from . import forms as F


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def api(request):
    print(str(request.path))
    if request.method == 'POST':
        form = F.SearchForm(request.POST)
        print(form)
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
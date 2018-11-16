import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UsersCollection
from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def api(request):
    reqpath = str(request.path)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            search = form.cleaned_data.get('search')
            result = '\n'.join(UsersCollection.search_user(search))
            print(result)
            return JsonResponse({'response': result})
        else:
            return JsonResponse({'reponse': 'invalid form'})

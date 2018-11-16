import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import UsersCollection


# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def api(request):
    reqpath = str(request.path)
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(reqpath, body)
        result = '\n'.join(UsersCollection.search_user(body['userid']))
        print(result)
    return JsonResponse({'response': result})

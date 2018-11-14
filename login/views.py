from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def api(request):
    reqpath = str(request.path)
    user_id = reqpath.split('/')[2]
    print(user_id)
    return JsonResponse({'foo': 'bar'})

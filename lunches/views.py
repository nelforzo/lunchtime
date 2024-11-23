from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
from .models import Lunch

# home page view
def home_page_view(request):
    return render(request, 'lunches/home.html')

def get_lunches(request):
    lunches = Lunch.objects.all().values()
    return JsonResponse(list(lunches), safe=False)

def delete_lunch(request, id):
    if request.method == 'DELETE':
        lunch = get_object_or_404(Lunch, id=id)
        lunch.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=405)

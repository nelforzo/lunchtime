from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Lunch

# home page view
def home_page_view(request):
    return render(request, 'lunches/home.html')

def get_lunches(request):
    lunches = Lunch.objects.all().values()
    return JsonResponse(list(lunches), safe=False)

def create_lunch(request):
    data = json.loads(request.body)
    Lunch.objects.create(name=data['name'], price=data['price'])
    return JsonResponse({'message': 'Lunch created successfully'})

def get_lunch(request, id):
    lunch = Lunch.objects.get(id=id)
    return JsonResponse({'lunch': lunch})

def update_lunch(request, id):
    data = json.loads(request.body)
    Lunch.objects.filter(id=id).update(name=data['name'], price=data['price'])
    return JsonResponse({'message': 'Lunch updated successfully'})

def delete_lunch(request, id):
    Lunch.objects.filter(id=id).delete()
    return JsonResponse({'message': 'Lunch deleted successfully'})
from django.urls import path
from .views import home_page_view, get_lunches, delete_lunch

urlpatterns = [
    path('home/', home_page_view, name='home'),
    # path for GET request to get all lunches
    path('lunches/', get_lunches, name='get_lunches'),
    # path for POST request to delete a lunch by id
    path('delete/<int:id>/', delete_lunch, name='delete_lunch'),
]

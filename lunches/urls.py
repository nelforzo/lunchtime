from django.urls import path
from .views import home_page_view, create_lunch, get_lunches, get_lunch, update_lunch, delete_lunch

urlpatterns = [
    path('home/', home_page_view, name='home'),
    # path for GET request to get all lunches
    path('lunches/', get_lunches, name='get_lunches'),
    # path for POST request to handle a json payload
    path('lunches/', create_lunch, name='create_lunch'),
    # path for GET request to get a single lunch by id
    path('lunches/<int:id>/', get_lunch, name='get_lunch'),
    # path for PUT request to update a lunch by id
    path('lunches/<int:id>/', update_lunch, name='update_lunch'),
    # path for DELETE request to delete a lunch by id
    path('lunches/<int:id>/', delete_lunch, name='delete_lunch'),
]

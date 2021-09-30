from django.urls import path
from .views import display,insert,delete,has

urlpatterns = [
    path('display', display,name='display'),
    path('insert/<int:zipcode>', insert,name='insert'),
    path('delete/<int:zipcode>', delete,name='delete'),
    path('has/<int:zipcode>', has,name='has'),
]
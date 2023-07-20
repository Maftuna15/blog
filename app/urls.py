from django.urls import path
from .views import *

urlpatterns=[
    path('form/', lala, name='form'),
    path('', forms, name='customerform'),
]
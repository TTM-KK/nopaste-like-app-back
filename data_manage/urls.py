from django.urls import path
from .views import *

urlpatterns = [
    path('', TextPostAPI.as_view()),
    path('display/<id>/', TextGetAPI.as_view()),
]

from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.api_home),
    path('list/',ListUsers.as_view())
]
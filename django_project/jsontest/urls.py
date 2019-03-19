from django.urls import path
from . import views

urlpatterns = [
    path('', views.json_view , name = "jsontests-json_view" ),
]

from django.urls import path
from .views import Homepage

app_name = "menu"

urlpatterns = [
    path("", Homepage.as_view(), name="home"),
]

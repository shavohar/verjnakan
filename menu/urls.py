from django.urls import path
from .views import ItemsListView

app_name = "menu"

urlpatterns = [
        path("", ItemsListView.as_view(), name="items"),
]

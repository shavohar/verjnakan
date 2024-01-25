from django.urls import path
from .views import AboutUsListView


app_name = 'aboutus'

urlpatterns = [
    path('about-us', AboutUsListView.as_view(), name='aboutus_list'),
]

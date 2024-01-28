from django.urls import path
from .views import Homepage, AboutUsView, ContactUsView

app_name = "home"

urlpatterns = [
    path("", Homepage.as_view(), name="home"),
    path('about-us', AboutUsView.as_view(), name='about_us'),
    path('contact-us', ContactUsView.as_view(), name='contact_us'),
]

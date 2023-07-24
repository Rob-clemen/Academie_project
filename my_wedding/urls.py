from django.urls import path
from .views import homeView,aboutView



urlpatterns = [
    path('',homeView, name="index" ),
    path('about/',aboutView,name="about")
]
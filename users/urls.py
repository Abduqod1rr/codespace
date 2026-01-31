from django.urls import path 
from .views import RegisterView ,login


urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path('login/',login.as_view(),name='login')
]

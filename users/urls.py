from django.urls import path 
from .views import RegisterView ,login,logoutuser


urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path('login/',login.as_view(),name='login'),
    path('logout/',logoutuser,name='logout')
]

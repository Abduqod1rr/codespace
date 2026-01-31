from django.urls import path
from .views import CodeFileListView


urlpatterns = [
    path("home/", CodeFileListView.as_view(), name="home")
]

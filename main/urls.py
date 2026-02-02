from django.urls import path
from .views import CodeFileListView,UpdateFile,CreateFile,FileDeleteView 


urlpatterns = [
    path("home/", CodeFileListView.as_view(), name="home"),
   
    path("create/", CreateFile.as_view(), name="create"),
    path("update/<int:pk>", UpdateFile.as_view(), name="update"),
    path("delete/<int:pk>", FileDeleteView.as_view(), name="delete"),
]

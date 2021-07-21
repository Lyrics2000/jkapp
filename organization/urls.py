
from django.urls import path
from .views import index,file_upload
app_name = 'organization'
urlpatterns = [
    path('', index, name = 'index'),
    path('upload/',file_upload,name= "upload_file"),
    

]



from django.urls import path
from .views import login

app_name = 'accounts'


urlpatterns = [
    path('',login,name= 'organization_login'),
    
    
]

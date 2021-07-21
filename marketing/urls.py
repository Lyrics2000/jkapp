
from django.urls import path
from .views import (index,new_applicants,delete_row)
app_name = 'marketing'
urlpatterns = [
    path('', index, name = 'index'),
    path('new_applicants',new_applicants,name ="new_applicants"),
    path('new_applicants/<slug>/', delete_row, name='delete_applicants'),

]

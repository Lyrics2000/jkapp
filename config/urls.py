
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls',namespace='accounts')),
    path('organization/',include('organization.urls',namespace='organization')),
    path('marketing/',include('marketing.urls',namespace='marketing')),
    path('security/',include('security.urls',namespace='security')),
]

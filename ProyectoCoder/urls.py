from django.contrib import admin
from django.urls import path,include

urlpatterns = [
path ('admin/', admin.site.urls),
path ('Web_Coder/', include('Web_Coder.urls')),
]
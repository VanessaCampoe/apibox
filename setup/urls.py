from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # importar a url 
    path('', include('apibox_app.urls')),
   
]

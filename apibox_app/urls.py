from django.urls import path
from apibox_app.views import box

urlpatterns = [
    path('box/', box, name='box'),
]
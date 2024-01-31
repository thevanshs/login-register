from django.contrib import admin
from django.urls import path
from logref.views import *

urlpatterns = [
    path('',register_page,name="register_page"),
    path('login/',login_page,name="login_page"),
    path('admin/', admin.site.urls),
]

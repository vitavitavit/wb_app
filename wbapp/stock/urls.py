from django.contrib import admin
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('goods/<int:gid>/', goods),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]

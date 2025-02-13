# blogs/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # it begins path with a blank url or the root (same as the mysite url start) -- If url has post_list in it, it will execute a function called post_list
]
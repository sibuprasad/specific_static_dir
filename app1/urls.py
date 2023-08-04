app_name='app1'

from django.urls import path
from app1.views import *

urlpatterns = [
    path('page1/',page1,name='page1'),
    path('page2/',page2,name='page2'),
]
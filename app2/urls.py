from django.urls import path,re_path
from app2.views import *
app_name='Radha_Rani'
# you can use re_path or path both
urlpatterns = [
    path('jinja_temp/',jinja_temp,name='jinja_temp'),
]

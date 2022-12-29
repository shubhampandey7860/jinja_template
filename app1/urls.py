from django.urls import path
from app1.views import jinja
urlpatterns = [
    path('jinja1/',jinja,name='jinja1'),
]


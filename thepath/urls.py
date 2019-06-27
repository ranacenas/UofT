from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^thepath/checkagain/$', views.checkagain, name='checkagain'),
]

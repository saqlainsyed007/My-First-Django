from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<name>[a-zA-z0-9 ]+)/$', views.content, name='content'),
]

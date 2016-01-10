from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^works$', views.works, name='works'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^profile$', views.profile, name='profile'),

]

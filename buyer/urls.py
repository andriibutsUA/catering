from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dish_id>[0-9]+)/$', views.dish, name='dish'),
    url(r'^dish_list$', views.dish_list, name='dish_list')
]
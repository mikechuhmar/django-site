from django.conf.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    re_path(r'^$', views.CartDetail, name='CartDetail'),
]

from django.urls import include
from django.urls import path, re_path
from . import views
urlpatterns = [
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    re_path(r'^$', views.ProductList, name='ProductList'),
]

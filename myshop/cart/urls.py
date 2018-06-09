from django.urls import re_path, path
from . import views
urlpatterns = [
    path('remove/<int:product_id>/', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    re_path(r'^$', views.CartDetail, name='CartDetail'),
]

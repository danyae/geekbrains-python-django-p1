from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^post/(?P<pk>\d+)/$', views.product, name='product'),
    path('product/add/', views.product_add, name='product_add'),
]

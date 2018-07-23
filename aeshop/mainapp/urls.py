from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^post/(?P<pk>\d+)/$', views.product, name='product'),
    re_path(r'^product/(?P<pk>\d+)/$',
            views.ProductDetail.as_view(), name='product_detail'),
    # path('product/add/', views.product_add, name='product_add'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/update/<int:pk>/',
         views.ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>/',
         views.ProductDelete.as_view(), name='product_delete'),
]

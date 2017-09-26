from django.conf.urls import url
from shop.views import *


app_name = 'shop'
urlpatterns = [
    url(r'^$', Product_list.as_view(), name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', Product_list.as_view(), name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', Product_detail.as_view(), name='product_detail'),

]

from . import views
from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'bakery'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.login, name='login'),
    url(r'^get_items/$',views.get_item, name='get_item'),
    url(r'^order_item/$',views.order_item, name='order_item'),
    url(r'^check_order_history/$',views.check_order_history, name='check_order_history'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
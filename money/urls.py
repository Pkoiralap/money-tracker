from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^index/$', views.index),
    url(r'^transactions/', views.view_transactions),
    url(r'^addtransaction/', views.add_transaction),
    url(r'^removetransactions/', views.remove_transaction),
]

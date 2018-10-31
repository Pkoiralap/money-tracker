from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^past-transactions/', views.past_transactions),
    url(r'^add-transactions/', views.add_transactions),
]

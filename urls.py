from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('owner_list', views.OwnerList.as_view(), name='owner_list'),
    path('create_owner',views.form_view,name='create_owner')
]

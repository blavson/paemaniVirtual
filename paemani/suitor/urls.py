from django.contrib import admin
from django.urls import path
from . import views

app_name ='suitor'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:suitor_id>/view',views.view_suitor, name='view'),
    path('<int:suitor_id>/edit',views.edit_suitor, name='edit'),
    path('create', views.create_suitor, name='create')
]

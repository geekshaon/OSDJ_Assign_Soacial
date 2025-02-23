# urls pattern for the app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('mypost/', views.mypost, name='mypost'),
    path('post/<int:id>/edit/', views.postupdate, name='edit_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
]
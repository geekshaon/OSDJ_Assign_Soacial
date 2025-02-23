from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(template_name='myauth/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.register, name='register'),
]
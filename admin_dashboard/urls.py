from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('add-user/', views.add_user, name='add_user'),
]

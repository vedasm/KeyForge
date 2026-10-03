from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.dashboard_view, name="dashboard"),
    path('add/', views.add_key, name="add_key"),
    path('update/<int:key_id>/', views.update_key, name="update_key"),
    path('delete/<int:key_id>/', views.delete_key, name="delete_key"),
    path('account/', views.account, name="account"),
]
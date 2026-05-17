from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # Novas rotas para o Magic Link
    path('magic-link/', views.magic_link_request_view, name='magic_link_request'),
    path('magic-login/<str:uidb64>/<str:token>/', views.magic_login_view, name='magic_login'),
]
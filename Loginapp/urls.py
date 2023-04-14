from django.urls import path

from Loginapp import views

urlpatterns= [
    path('',views.home),
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('readregister',views.read_register,name='readregister'),
    path('readlogin',views.read_login,name='readlogin'),
    path('logout',views.logout_fun,name='logout')
]
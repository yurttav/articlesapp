from django.contrib import admin
from django.urls import path

from . import views
#isim verme önemli redirect için 
app_name = "user"

urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
]
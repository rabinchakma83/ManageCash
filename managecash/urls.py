from django.urls import path
from managecash.views import home,register,User_Login,user_logout

urlpatterns = [
    path('home/',home, name='home'),
    path('register/',register, name='register'),
    path('login/',User_Login, name='userlogin'),
    path('logout/',user_logout, name='userlogout'),
]
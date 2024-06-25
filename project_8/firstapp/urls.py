from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='hompages'),
    path('signup/',views.SignUp_pages,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('profile/',views.Profile,name='profile'),
    path('passchanges/',views.passWord_changes,name='passWord_changes'),
    path('passchanges2/',views.passWord_changes2,name='passWord_changes2'),


   
]
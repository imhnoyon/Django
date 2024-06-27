from django.urls import path
from . import views
urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.user_login,name='login'),
   path('profile/',views.profile,name='profile'),
   path('profile/edit',views.Edit_profile,name='editprofile'),
   path('logout/',views.Logout,name='logout'),
   path('pass_change/',views.pass_change,name='pass_change'),
]




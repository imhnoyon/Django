from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.Home,name='homepages'),
    path('get/',views.get_cookie),
    path('delete/',views.delete_cookies),
    path('session/',views.set_session),
    path('get/session/',views.get_session),
    path('del/session/',views.delete_session),
]
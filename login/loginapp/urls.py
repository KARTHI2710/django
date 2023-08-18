from django.contrib.auth import views as auth_views
#from django.contrib.auth.urls import views as auth_views
from django.urls import path
from .views import loginresponse
urlpatterns = [
    
    path('',auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('home/',loginresponse,name="loginresponse")
    #path('home',views.loginresponse)
]

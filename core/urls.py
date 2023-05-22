from django.urls import path
from .views import *
from django.contrib.auth import views
#from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('acceder/',acceder,name="acceder"),
    path('logout/',LogOut,name='logout'),
    path('',home,name="home"),
    path('registro/',registro,name="registro"),
    path('consultas/',consultas,name="consultas"),
    path('reset_password/', resetpassword, name='resetpassword'),
    path('reset_password/request', resetpassword_request, name='resetpassword_request'),
    path('change-password/<token>/', resetpassword_reset, name='resetpassword_reset')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

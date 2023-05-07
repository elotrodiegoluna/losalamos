from django.urls import path
from .views import home, acceder, LogOut, registro
from django.contrib.auth import views
#from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('acceder/',acceder,name="acceder"),
    path('logout/',LogOut,name='logout'),
    path('',home,name="home"),
    path('registro/',registro,name="registro"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

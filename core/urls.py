from django.urls import path
<<<<<<< HEAD
from .views import home, acceder, LogOut, registro, consultas,obtener,create_event
=======
from .views import home, acceder, LogOut, registro, consultas
>>>>>>> segundaMedica
from django.contrib.auth import views
#from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('acceder/',acceder,name="acceder"),
    path('logout/',LogOut,name='logout'),
    path('',home,name="home"),
    path('registro/',registro,name="registro"),
<<<<<<< HEAD
    path('consultas/',consultas,name="consultas"),
    path('calendario/',obtener,name="calendario"),
    path('event/<int:user_id>',create_event,name="event")
=======
    path('consultas/',consultas,name="consultas")
>>>>>>> segundaMedica

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

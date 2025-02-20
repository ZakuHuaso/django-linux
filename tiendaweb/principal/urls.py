from django.urls import path
from . import views

urlpatterns = [
path('',views.home, name='inicio'),
path('registro/',views.registro, name='registro'),
path('login/',views.inicio_sesion, name='login'),
path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
path('contacto/',views.contact, name='contacto'),
path('perfil/',views.perfilvista, name='perfil'),
path('ofertas/',views.ofertas, name='ofertas'),
path('productos',views.productos, name='productos')
]

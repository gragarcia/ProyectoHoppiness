from atexit import register
from django.urls import path
from AppHoppiness import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("login", views.login_request, name="Login"),
    path("logout", LogoutView.as_view(template_name='AppHoppiness/logout.html'), name="Logout"),
    path("register", views.registrar, name="Registro"),
    path("editarUsuario/", views.editarUsuario, name='EditarUsuario'),
    path("about/", views.about, name='AcercaDeMi'),

    path("bebidas/", views.bebida, name='Bebidas'),
    path(r'^guardar$', views.BebidaCreacion.as_view(), name='CrearBebida'),
    path("bebidas/lista", views.BebidaLista.as_view(), name='ListaBebidas'),
    path(r'^(?P<pk>\d+)$', views.BebidaDetalle.as_view(), name='DetalleBebida'),
    path(r'^borrar/(?P<pk>\d+)$', views.BorrarBebida.as_view(), name='BorrarBebida'),
    path(r'^editar/(?P<pk>\d+)$', views.BebidaEdicion.as_view(), name='EditarBebida'),
    
    #path("comidas/", views.comida, name='Comidas'),
    path(r'^guardar$', views.ComidaCreacion.as_view(), name='CrearComida'),
    path("comidas/lista", views.ComidaLista.as_view(), name='ListaComidas'),
    path(r'^(?P<pk>\d+)$', views.ComidaDetalle.as_view(), name='DetalleComida'),
    path(r'^borrar/(?P<pk>\d+)$', views.BorrarComida.as_view(), name='BorrarComida'),
    path(r'^editar/(?P<pk>\d+)$', views.ComidaEdicion.as_view(), name='EditarComida'),
    
    #path("valoraciones/", views.valoraciones, name='Valoraciones'),
    path("valoraciones/lista", views.ValoracionLista.as_view(), name='ListaValoraciones'),
    
    path("eventos/", views.evento, name='Eventos'),
    path("promos/", views.promo, name='Promos'),
    
]
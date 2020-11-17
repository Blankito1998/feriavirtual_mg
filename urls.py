from django.urls import path
from feriavirtual import  views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('', views.login, name='login'),
   path('informacion/', views.informacion, name = 'informacion'),
   path('administrador/',views.administrador,name = 'administrador'),
   path('olvidoContrasena/',views.olvidoContrasenia,name = 'olvidoContrasenia'),
   path('nuevaContrasenia/', views.nuevaContrasenia,name = 'nuevaContrasenia'),
   path('administrarUsuario/',views.administrarUsuario, name = 'administrarUsuario'),
   path('registarUsuario/',views.registrarUsuario, name = 'registrarUsuario'),
   path('listarUsuario/',views.listarUsuario, name = 'listarUsuario'),
   path('edicionUsuario/<rut>',views.edicionUsuario, name = 'edicionUsuario'),
   path('eliminarUsuario/<rut>', views.eliminarUsuario, name = 'eliminarUsuario'),
   path('registrarUsuario/',views.registrarUsuario, name = 'registrarUsuario'),
   path('administrarVentas/',views.administrarVentas,name = 'administrarVentas'),
   path('solicitudCompraExterior/',views.listarSolicitudCompra,name = 'solicitudCompraExterior'),
   path('productor/',views.baseProductor,name= 'productor'),
   path('consultor/',views.baseConsultor, name = 'consultor'),
   path('transportista/',views.baseTransportista, name = 'transportista'),
   path('clienteExterno/',views.baseClienteExterno, name = 'clienteExterno'),
   path('clienteInterno/', views.baseClienteInterno, name = 'clienteInterno'),
   path('ingresarProductos/',views.ingresarProcuto, name = 'ingresarProductos'),
   path('solicitudCompraInterior/',views.listarSolicitudCompraInterior, name ='solicitudCompraInterior'),
   path('solicitudCompraTodos/',views.listarTodaSolicutud, name = 'solicitudCompraTodos'),
   path('listarProductor/',views.listarProductores, name = 'listarProductor'),
   path('subastaAdministrador/',views.subastaGanadador, name ='subastaAdministrador'),
]
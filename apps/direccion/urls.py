from django.urls import path
from .views import (vLogin, vLogout, vPrinDirec, vPerfil, vCambiarAvatar, vCambiarNombreUsuario, vCambiarPassword,
                    vRegistroActividades, vEliminarActividades, vEditarActividad, vObtenerActividades,
                    vEditarCheckObjetivo, vEliminarObjetivo, vEditarObjetivo, vAgregarObjetivos, vEditarComentario,
                    vRegistroUsuarios, vAgregarEvidencias, vEliminarEvidencias,)
from .download_evidences import descargarEvidenciasZip
app_name = 'direccion'

urlpatterns = [
    path('', vPrinDirec, name = 'prinDirect'),
    path('acceso/', vLogin, name = "login"),
    path('logout/', vLogout, name = 'logout'),
    path('registro/', vRegistroUsuarios, name = 'rUsuario'),
    path('perfil/', vPerfil, name = 'perfil'),
    #Activities
    path('actividad/agregar', vRegistroActividades, name = 'rActividad'),
    path('actividad/<int:id>/eliminar', vEliminarActividades, name = 'eActividad'),
    #Objetivos
    path('actividad/objetivo/<int:id>/eliminar', vEliminarObjetivo, name = 'eObjetivo'),
    #Evidencias
    path('actividad/evidencias/agregar', vAgregarEvidencias, name = 'rEvidencia'),
    path('actividad/evidencias/<int:id>/eliminar', vEliminarEvidencias, name = 'eEvidencia'),
    path('actividad/<int:id>/evidencias/descargar', descargarEvidenciasZip, name = 'desEvidencias'),
    #Ajax
    path('ajax/actividad/objetivo/editarcheck', vEditarCheckObjetivo),
    path('ajax/actividad/<int:id>/editar', vEditarActividad, name = 'edActividad'),
    path('ajax/actividad/objetivo/<int:id>/editar', vEditarObjetivo, name = 'edObjetivo'),
    path('ajax/actividad/objetivo/agregar', vAgregarObjetivos, name = 'aObjetivo'),
    path('ajax/actividades/', vObtenerActividades, name = 'obActividades'),
    path('ajax/actividad/<int:id>/comentarios/editar', vEditarComentario, name = 'eComentario'),
    #vERIFICAR
    path('titular/avatar/cambiar', vCambiarAvatar, name = 'eAvatar'),
    path('titular/nombre/cambiar', vCambiarNombreUsuario, name = 'eNombreUsu'),
    path('titular/password/cambiar', vCambiarPassword, name = 'ePassword'),

]
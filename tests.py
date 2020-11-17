from MaipoGrandeWeb import  wsgi
from django.test import TestCase
from feriavirtual.models import Usuario, CodigoRecuperacion, Usuariorol, Rolles, Productos, Solicituddecompra, \
    Subastacontransportista, Procesosubasta, Ingresodeproductos
import  hashlib
from django.db import connection

# Create your tests here.

mail = 'ale.sanhuezab@gmail.com'
codigo = 78216851
contraseña = 'holamundo'
contraseña = contraseña.encode("utf-8")

codificado = hashlib.md5(contraseña)
codificado = codificado.hexdigest()
codificado = str(codificado)

#tipoUsuario = Rolles.objects.get(idrol = request.POST.get('rol'))
#        rutroluser = Usuario.objects.get(rutopasaporte = request.POST.get('rut'))
#        usuarioRol = Usuariorol()
#        usuarioRol.rutopasaporte = tipoUsuario
#        usuarioRol.idrol = rutroluser
#        usuarioRol.save()


#rut = 17944235
#rol = 2
#rol2 = Rolles.objects.get(idrol=rol)
#rut2 = Usuario.objects.get(rutopasaporte=rut)



#try:
#    usuarioRol = CodigoRecuperacion.objects.get(codigo=codigo)
#    if codigo == usuarioRol.codigo:
#        if mail == usuarioRol.correo:
#            print( 'Correo y codigo correctos' )
#        else:
 #           print('datos no validos')
#
#
#except Exception as e:
 #   print('codigo no existente')




mail = 'ale.sanhuezab@gmail.com'
password = 'kaitokid85'

try:
    usuario = Usuario.objects.get(correo=mail)

    password = password.encode("utf-8")

    password = hashlib.md5(password)
    password = password.hexdigest()
    password = str(password)



    if password == usuario.contrasenia:

        rol = Usuariorol.objects.get(rutopasaporte=usuario.rutopasaporte)
        roles = rol.idrol
        roles = str(roles)
        roles = list(roles)
        roles = roles[15]
        roles = int(roles)
        print(roles)



        if roles == 1:

            print('El usuario '+usuario.nombre1 + ' es un Aministrador')
        elif roles == 2:

            print('El usuario ' + usuario.nombre1 + ' es un Productor')

        elif roles == 3:

            print('El usuario ' + usuario.nombre1 + ' es un Cliente Externo')
        elif roles == 4:

            print('El usuario ' + usuario.nombre1 + ' es un Cliente Interno')

        elif roles == 5:

            print('El usuario ' + usuario.nombre1 + ' es un Transportista')

        elif roles == 6:

            print('El usuario ' + usuario.nombre1 + ' es un Consultor')

        else:

            print('El usuario ' + usuario.nombre1 + ' No tiene rol asignado')

    else:

        print('Contraseña incorrecta')
except Exception as e:

    print('El correo ingresado no esta registrado')







solicitud = Solicituddecompra.objects.all()

a = []

for i in solicitud:

    u = Usuariorol.objects.get(rutopasaporte=i.rutopasaporte_id)

    if u.idrol.idrol == 3:


        a.append(i)




ganador = Subastacontransportista.objects.all()
cursor = connection.cursor()
cursor.execute('proc_buscarSubastaFinal')
results = cursor.fetchall()

print(results)


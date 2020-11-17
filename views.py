from unittest import result

from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import logout as do_logout
from feriavirtual.models import CodigoRecuperacion
import smtplib
from email.mime.text import MIMEText
import random
# Create your views here.
from feriavirtual.models import Usuario, Productos, CodigoRecuperacion,Rolles,Usuariorol,Solicituddecompra,Ingresodeproductos,Procesosubasta, Ganadorsubasta, Subastacontransportista
from feriavirtual.forms import FormularioUsuario,FormularioCrearUsuario
from django.contrib import messages
import hashlib
from django.db.models import Q
from datetime import datetime
from django.db import connection
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO

def login(request):

    try:


        if request.method == 'POST':

            mail = request.POST.get('mail')
            password = request.POST.get('contrasenia')
            password = password.encode("utf-8")
            password = hashlib.md5(password)
            password = password.hexdigest()
            password = str(password)

            usuario = Usuario.objects.get(correo=mail)

            if password == usuario.contrasenia:

                try :
                    rol = Usuariorol.objects.get(rutopasaporte=usuario.rutopasaporte)

                    rol = rol.idrol
                    rol = str(rol)
                    rol = list(rol)
                    rol = rol[15]
                    rol = int(rol)

                    if rol == 1:

                        return redirect(to='administrador')

                    elif rol == 2:

                        return redirect(to='productor')

                    elif rol == 3:

                        return redirect(to='clienteExterno')

                    elif rol == 4:

                        return redirect(to='clienteInterno')

                    elif rol == 5:

                        return redirect(to='transportista')

                    elif rol == 6:

                        return redirect(to='consultor')

                except Exception as e:

                    messages.success(request, 'Este usuario no tiene un rol asignado contactese con el administrador')



            else:

                messages.success(request, 'Asegurese que los datos ingresados sean correctos')




    except Exception as e:

        messages.success(request, 'Asegurese que los datos ingresados sean correctos')




    return  render(request, 'Login.html')


def informacion(request):

    return  render(request, 'Informacion.html')

def administrador(request):

    return  render(request,'BaseAdministrador.html')


def olvidoContrasenia(request):

    try:

        if request.method == 'POST':

            mail = request.POST.get('mail')
            usuario = Usuario.objects.get(correo=mail)

            if mail == usuario.correo:
                send_email(mail)
                messages.success(request, 'Correo enviado con éxito.')
                return redirect(to = 'nuevaContrasenia')


    except Exception as e:
        messages.error(request, 'Ocurrió un error al enviar el correo asegurese de ungresar un correo valio')

    return render(request, 'OlvidoContrasenia.html')

def nuevaContrasenia(request):


    try:

        if request.method == 'POST':
            mail = request.POST.get('CorrUsuario')
            codigo = request.POST.get('Codigo')
            contra = request.POST.get('Contraseña1')
            contra = contra.encode("utf-8")
            contra = hashlib.md5(contra)
            contra = contra.hexdigest()
            contra = str(contra)

            contra2 = request.POST.get('Contraseña2')
            contra2 = contra2.encode("utf-8")
            contra2 = hashlib.md5(contra2)
            contra2 = contra2.hexdigest()
            contra2 = str(contra2)

            recuperacion = CodigoRecuperacion.objects.get(codigo=codigo)


            if mail == recuperacion.correo:
                usuario = get_object_or_404(Usuario, correo=mail)
                usuario.contrasenia = contra
                if contra == contra2:
                    usuario.save()
                    recuperacion.delete()

                    return redirect(to='login')
                else:

                    messages.error(request, 'Las contraseñas no son iguales')

            else:

                messages.error(request, 'El correo no pertenece al codigo ingresado')

    except Exception as e:

        messages.error(request, 'El codigo ingresado no es valido')

    return render(request,'NuevaContrasenia.html')


def send_email(mail):
    Recuperacion = random.random() * (99999999 - 100 + 1)
    Recuperacion = int(Recuperacion)
    codigo = CodigoRecuperacion(correo=mail, codigo=Recuperacion)
    codigo.save()
    Recuperacion = str(Recuperacion)
    try:
        emailEviar = "contacto.feriavirtual.mg@gmail.com"
        emailContrasenia = "maipogrande1"
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(emailEviar, emailContrasenia)

        mensaje = MIMEText(
            "Haz solicitado la recuperacion de tu contraseña, usa el siguiente codigo para recuperarla: " + Recuperacion)
        mensaje['From'] = "contrasenamaipogrande@gmail.com"
        mensaje['To'] = mail
        mensaje['Subject'] = "Peticion cambio de contraseña"

        mailServer.sendmail("contrasenamaipogrande@gmail.com",
                            mail,
                            mensaje.as_string())




    except Exception as e:
        print(e)


def administrarUsuario(request):

    return render(request,'AdministrarUsuario.html')


def listarUsuario(request):


    usuarios = Usuario.objects.all()

    rut = request.GET.get('rut')

    if rut:
        usuarios = Usuario.objects.filter(

            Q(rutopasaporte=rut)

        ).distinct()



    data = {
        'usuarios':usuarios
    }
    return  render(request,'ListarUsuario.html',data)


def edicionUsuario(request,rut):

    usuario = get_object_or_404(Usuario,rutopasaporte=rut )

    data = {
        'form': FormularioUsuario(instance=usuario)

    }

    if request.method == 'POST':
        formulario = FormularioUsuario(data = request.POST,instance=usuario)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarUsuario')

    return render(request,'EdicionUsuario.html',data)

def eliminarUsuario(request,rut):

    usuario = get_object_or_404(Usuario, rutopasaporte=rut)
    usuarioRol = get_object_or_404(Usuariorol, rutopasaporte=rut)
    usuarioRol.delete()
    usuario.delete()

    return redirect(to='listarUsuario')

def registrarUsuario(request):

    data = {
        'form': FormularioCrearUsuario()
    }
    if request.method == 'POST':

        rut = request.POST.get('rut')
        dv = request.POST.get('digito')
        primerNombre = request.POST.get('pnombre')
        segundoNombre = request.POST.get('snombre')
        apellidoP = request.POST.get('ap')
        apellidoM = request.POST.get('am')
        mail = request.POST.get('correo')
        contra = request.POST.get('contrasenia')

        contra = contra.encode("utf-8")
        contra = hashlib.md5(contra)
        contra = contra.hexdigest()
        contra = str(contra)

        usuario = Usuario(rutopasaporte=rut,dv=dv,nombre1=primerNombre,nombre2=segundoNombre,appaterno=apellidoP,apmaterno=apellidoM,correo=mail,contrasenia=contra)
        usuario.save()

        rol1 = request.POST.get('rol')
        rol2 = Rolles.objects.get(idrol=rol1)
        rut2 = Usuario.objects.get(rutopasaporte=rut)

        usuarioRol = Usuariorol(idrol=rol2,rutopasaporte=rut2)
        usuarioRol.save()






        return redirect(to='listarUsuario')

    return render(request,'RegistrarUsuario.html',data)


def administrarVentas (request):

    return render(request, 'AdministrarVentas.html')

def listarSolicitudCompra (request):

    solicitudes = Solicituddecompra.objects.all()
    solicitud = []

    productos = Ingresodeproductos.objects.all()
    productosCantidad = []


    for i in solicitudes:

        u = Usuariorol.objects.get(rutopasaporte=i.rutopasaporte_id)

        if u.idrol.idrol == 3:
            if i.activo == 1:
                solicitud.append(i)

    for p in productos:

        if p.cantidad > 0:
            productosCantidad.append(p)



    buscarSolicitud = request.GET.get('idSolcitud2')




    if buscarSolicitud:

        solicitud = Solicituddecompra.objects.filter(

            Q(rutopasaporte= buscarSolicitud)

        ).distinct()

    buscarProducto = request.GET.get('idProducto2')

    if buscarProducto:

        productosCantidad = Ingresodeproductos.objects.filter(

            Q(idproducto_id= buscarProducto)

        ).distinct()

    data = {
        'solicitud': solicitud,
        'productos': productosCantidad
    }


    if request.method == 'POST':

        solicitudId = request.POST.get('idSolcitud')
        productoId =  request.POST.get('idProducto')

        procesoSolicitud = Solicituddecompra.objects.get(idsolicitud=solicitudId)
        procesoProducto = Ingresodeproductos.objects.get(idingresoproducto=productoId)

        if procesoSolicitud.idproducto == procesoProducto.idproducto:

            if  procesoProducto.cantidad >= procesoSolicitud.cantidad:

                cant = procesoSolicitud.cantidad

                vUnidad = procesoProducto.precioporunidad

                precioTotal = cant* vUnidad

                procesoSubasta = Procesosubasta(idsolicitud= procesoSolicitud,idingresodeproductos=procesoProducto,cantidad=cant,valorporunidad=vUnidad,total=precioTotal, activo= 1 )
                procesoSubasta.save()

                actualizarSolicitud = get_object_or_404(Solicituddecompra, idsolicitud=solicitudId)
                actualizarSolicitud.activo = 0
                actualizarSolicitud.save()

                actualizarIngreso = get_object_or_404(Ingresodeproductos,idingresoproducto=productoId)

                cantidadActual = procesoProducto.cantidad - procesoSolicitud.cantidad

                if cantidadActual == 0:

                    actualizarIngreso.cantidad = cantidadActual
                    actualizarIngreso.activo = 0
                    actualizarIngreso.save()
                else:
                    actualizarIngreso.cantidad = cantidadActual
                    actualizarIngreso.save()

                messages.success(request, 'Proceso de venta creado con exito')

            else:

                messages.error(request, 'El productor no tiene el suficiente stock del producto que se requiere ,porfavor seleccione otro')

        else:

            messages.error(request, 'Asegurese de elegir el producto que esta pidiendo el Cliente Externo')


    return  render(request, 'SolicitudCompraExterior.html', data)


def listarSolicitudCompraInterior (request):

    solicitudes = Solicituddecompra.objects.all()
    solicitud = []

    productos = Ingresodeproductos.objects.all()
    productosCantidad = []


    for i in solicitudes:

        u = Usuariorol.objects.get(rutopasaporte=i.rutopasaporte_id)

        if u.idrol.idrol == 4:
            if i.activo == 1:

                solicitud.append(i)


    for p in productos:

        if p.activo == 1:

            productosCantidad.append(p)



    buscarSolicitud = request.GET.get('idSolcitud2')




    if buscarSolicitud:

        solicitud = Solicituddecompra.objects.filter(

            Q(rutopasaporte= buscarSolicitud)

        ).distinct()

    buscarProducto = request.GET.get('idProducto2')

    if buscarProducto:

        productos = Ingresodeproductos.objects.filter(

            Q(idproducto_id= buscarProducto)

        ).distinct()

    data = {
        'solicitud': solicitud,
        'productos': productosCantidad
    }


    if request.method == 'POST':

        solicitudId = request.POST.get('idSolcitud')
        productoId =  request.POST.get('idProducto')

        procesoSolicitud = Solicituddecompra.objects.get(idsolicitud=solicitudId)
        procesoProducto = Ingresodeproductos.objects.get(idingresoproducto=productoId)

        if procesoSolicitud.idproducto == procesoProducto.idproducto:

            if procesoProducto.cantidad >= procesoSolicitud.cantidad:

                cant = procesoSolicitud.cantidad

                vUnidad = procesoProducto.precioporunidad

                precioTotal = cant* vUnidad

                procesoSubasta = Procesosubasta(idsolicitud= procesoSolicitud,idingresodeproductos=procesoProducto,cantidad=cant,valorporunidad=vUnidad,total=precioTotal, activo= 1 )
                procesoSubasta.save()

                actualizarSolicitud = get_object_or_404(Solicituddecompra, idsolicitud=solicitudId)
                actualizarSolicitud.activo = 0
                actualizarSolicitud.save()

                actualizarIngreso = get_object_or_404(Ingresodeproductos, idingresoproducto=productoId)

                cantidadActual = procesoProducto.cantidad - procesoSolicitud.cantidad

                if cantidadActual == 0:

                    actualizarIngreso.cantidad = cantidadActual
                    actualizarIngreso.activo = 0
                    actualizarIngreso.save()
                else:
                    actualizarIngreso.cantidad = cantidadActual
                    actualizarIngreso.save()



            else:

                messages.error(request,  'El productor no tiene el suficiente stock del producto que se requiere ,porfavor seleccione otro')

        else:

            messages.error(request, 'Asegurese de elegir el producto que esta pidiendo el Cliente Interno')




    return  render(request, 'SolicitudCompraInterior.html', data)



def listarTodaSolicutud (request):

    solicitudes = Solicituddecompra.objects.all()
    soliciud = []

    for i in solicitudes:

        if i.activo == 1:

            soliciud.append(i)

    filtro = request.GET.get('filtro')

    if filtro:

        soliciud = Solicituddecompra.objects.filter(
            Q(rutopasaporte=filtro) & Q(activo=1)
        ).distinct()


    data = {
        'solicitud': soliciud
    }


    return render(request,'SolicitudCompraTodos.html',data)


def listarProductores ( request ):
    productos = Ingresodeproductos.objects.all()
    productosCantidad = []
    buscarProductor = request.GET.get('idProductor')

    for p in productos:
        if p.activo == 1:

            productosCantidad.append(p)

    if buscarProductor:
        productos = Ingresodeproductos.objects.filter(

            Q(rutopasaporte=buscarProductor)

        ).distinct()

    data = {

        'productos': productosCantidad
    }



    return render(request,'ListaProductor.html',data)




def baseClienteExterno (request):

    return  render(request,'BaseClienteExterno.html')


def baseClienteInterno(request):
    return render(request, 'BaseClienteInterno.html')


def baseConsultor(request):
    return render(request, 'BaseConsultor.html')


def baseProductor(request):
    return render(request, 'BaseProductor.html')


def baseTransportista(request):
    return render(request, 'BaseTransportista.html')

def ingresarProcuto(request):

    productos = Productos.objects.all()

    data = {
        'productos' : productos
    }


    p = request.POST.get('producto')
    cantidad = request.POST.get('cantidad')
    precio = request.POST.get('precio')


    return render(request,'IngresarProductos.html',data)


def subastaGanadador (request):


    ganador = Subastacontransportista.objects.all().order_by('valor')#.filter(activo=1)

    subasta = request.GET.get('idSubasta')

    if subasta:
        ganador = Subastacontransportista.objects.filter(

            Q(idsubasta=subasta)

        ).distinct().order_by('valor')

    data = {
        'ganador' : ganador,
    }

    if request.method == 'POST':

        try:
            nuevoGanador = request.POST.get('idPart')
            ganadorSubasta = Subastacontransportista.objects.get(idsubastafinal= nuevoGanador)
            solicitud = Procesosubasta.objects.get(idsubasta=ganadorSubasta.idsubasta.idsubasta)


            valorViaje1 = ganadorSubasta.valor
            valorFruta1 = solicitud.total
            valorTotal1 = valorViaje1 + valorFruta1

            ganadorFinal = Ganadorsubasta( idparticipacion= ganadorSubasta, valortotal= valorTotal1,valortotalviaje=valorViaje1,
                                           valortotalfruta=valorFruta1,estado='Por Pagar', estadocliente='No Recibido', tarjeta='',cvv='',fecha='', activo=1)

            ganadorFinal.save()
            messages.success(request, 'Agregado correctamente')

        except Exception as e:

            messages.error(request, 'El id subasta final no existe')

    return render(request,'SubastasAdministrador.html',data)

def pdf(template_src, context_dict={}):
    resultado = BytesIO()
    template = get_template(template_src)
    html = template.render(context_dict)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), resultado)
    if not pdf.err:
        return  HttpResponse(resultado.getvalue(),content_type='application/pdf')

    return None
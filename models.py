# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ganadorsubasta(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idparticipacion = models.ForeignKey('Subastacontransportista', models.DO_NOTHING, db_column='IdParticipacion')  # Field name made lowercase.
    valortotal = models.IntegerField(db_column='Valortotal')  # Field name made lowercase.
    valortotalfruta = models.IntegerField(db_column='ValorTotalFruta')  # Field name made lowercase.
    valortotalviaje = models.IntegerField(db_column='ValorTotalViaje')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50)  # Field name made lowercase.
    estadocliente = models.CharField(db_column='EstadoCliente', max_length=50)  # Field name made lowercase.
    tarjeta = models.CharField(db_column='Tarjeta', max_length=50)  # Field name made lowercase.
    cvv = models.CharField(db_column='Cvv', max_length=50)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=50)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GanadorSubasta'


class Ganancias(models.Model):
    idganancias = models.AutoField(db_column='IdGanancias', primary_key=True)  # Field name made lowercase.
    idganadorsubasta = models.ForeignKey(Ganadorsubasta, models.DO_NOTHING, db_column='IdGanadorSubasta')  # Field name made lowercase.
    rutopasaporte = models.ForeignKey('Usuariorol', models.DO_NOTHING, db_column='RutOPasaporte')  # Field name made lowercase.
    dinero = models.IntegerField(db_column='Dinero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ganancias'


class Ingresodeproductos(models.Model):
    idingresoproducto = models.AutoField(db_column='IdIngresoProducto', primary_key=True)  # Field name made lowercase.
    precioporunidad = models.IntegerField(db_column='PrecioPorUnidad')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='IdProducto')  # Field name made lowercase.
    rutopasaporte = models.ForeignKey('Usuariorol', models.DO_NOTHING, db_column='RutOPasaporte')  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IngresoDeProductos'


class Procesosubasta(models.Model):
    idsubasta = models.AutoField(db_column='IdSubasta', primary_key=True)  # Field name made lowercase.
    idsolicitud = models.ForeignKey('Solicituddecompra', models.DO_NOTHING, db_column='IdSolicitud')  # Field name made lowercase.
    idingresodeproductos = models.ForeignKey(Ingresodeproductos, models.DO_NOTHING, db_column='IdIngresoDeProductos')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    valorporunidad = models.IntegerField(db_column='ValorPorUnidad')  # Field name made lowercase.
    total = models.IntegerField(db_column='Total')  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProcesoSubasta'


class Productos(models.Model):
    idproducto = models.AutoField(db_column='IdProducto', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Productos'


class Resumendeventapdf(models.Model):
    idpdf = models.AutoField(db_column='IdPDF', primary_key=True)  # Field name made lowercase.
    idganadorsubasta = models.ForeignKey(Ganadorsubasta, models.DO_NOTHING, db_column='IdGanadorSubasta')  # Field name made lowercase.
    nombrepdf = models.CharField(db_column='NombrePDF', max_length=50)  # Field name made lowercase.
    archivopdf = models.BinaryField(db_column='ArchivoPDF')  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResumenDeVentaPDF'


class Rolles(models.Model):
    idrol = models.IntegerField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rolles'


class Solicituddecompra(models.Model):
    idsolicitud = models.AutoField(db_column='IdSolicitud', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100)  # Field name made lowercase.
    fecha_inicio = models.CharField(db_column='Fecha_inicio', max_length=50)  # Field name made lowercase.
    fecha_termino = models.CharField(db_column='Fecha_Termino', max_length=50)  # Field name made lowercase.
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='IdProducto')  # Field name made lowercase.
    rutopasaporte = models.ForeignKey('Usuariorol', models.DO_NOTHING, db_column='RutOPasaporte')  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolicitudDeCompra'


class Subastacontransportista(models.Model):
    idsubastafinal = models.AutoField(db_column='IdSubastaFinal', primary_key=True)  # Field name made lowercase.
    idsubasta = models.ForeignKey(Procesosubasta, models.DO_NOTHING, db_column='IdSubasta')  # Field name made lowercase.
    rutopasaporte = models.ForeignKey('Usuariorol', models.DO_NOTHING, db_column='RutOPasaporte')  # Field name made lowercase.
    tamano = models.IntegerField(db_column='Tamano')  # Field name made lowercase.
    capacidad = models.IntegerField(db_column='Capacidad')  # Field name made lowercase.
    refrigeracion = models.IntegerField(db_column='Refrigeracion')  # Field name made lowercase.
    valor = models.IntegerField(db_column='Valor')  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubastaConTransportista'


class Usuario(models.Model):
    rutopasaporte = models.IntegerField(db_column='RutOPasaporte', primary_key=True)  # Field name made lowercase.
    dv = models.IntegerField()
    nombre1 = models.CharField(db_column='Nombre1', max_length=50)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='Nombre2', max_length=50)  # Field name made lowercase.
    appaterno = models.CharField(db_column='ApPaterno', max_length=50)  # Field name made lowercase.
    apmaterno = models.CharField(db_column='ApMaterno', max_length=50)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=50)  # Field name made lowercase.
    contrasenia = models.CharField(db_column='Contrasenia', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class Usuariorol(models.Model):
    rutopasaporte = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='RutOPasaporte', primary_key=True)  # Field name made lowercase.
    idrol = models.ForeignKey(Rolles, models.DO_NOTHING, db_column='idRol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioRol'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CodigoRecuperacion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    correo = models.CharField(max_length=50)
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codigo_recuperacion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

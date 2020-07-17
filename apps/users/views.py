from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.core import mail
from apps.covid.models import *
from .forms import FormFiltrar
from datetime import date, datetime

departamentos = Departamento.objects.all()
municipios = Municipio.objects.all()

def login(request):

	if(request.method == 'POST'):

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.error(request,'Credenciales inválidas')
			return redirect('/')

	else:
		return render(request,'users/login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')

def gestion_laboratorista(request):	
	if(request.user.is_authenticated and request.user.rol == 0):
		laboratoristas = Laboratorista.objects.all()
		contexto = {'laboratoristas': laboratoristas,}
		return render(request, 'gestion_usuarios/gestion_laboratorista.html', contexto)
	else:
		contexto = {}
		return redirect('/')

def eliminar_laboratorista(request):

	Laboratorista.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_laboratorista')

def registrar_laboratorista(request):

	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	dui = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 1

	user, laboratorista = User.objects.get_or_create(
		username = usuario,
		first_name = nombre,
		last_name = apellido,
		email = correo,
		password = password,
		dui = dui,
		direccion = direccion,
		rol = rol,
		is_active = activo,
		is_staff = staff
	)
	
	if laboratorista:
		user.set_password(password)
		user.save()

	covid_laboratorista = Laboratorista()

	covid_laboratorista.user = user

	covid_laboratorista.save()

	if request.user.is_authenticated:

		return redirect('gestion_laboratorista')

	else:
		
		return redirect('/')

def editar_laboratorista(request):

	laboratorista = Laboratorista.objects.get(pk=request.POST['id_edit'])

	laboratorista.user.first_name = request.POST['nombre_edit']
	laboratorista.user.last_name = request.POST['apellido_edit']
	laboratorista.user.username = request.POST['usuario_edit']
	laboratorista.user.email = request.POST['correo_edit']
	laboratorista.user.dui = request.POST['telefono_edit']
	laboratorista.user.direccion = request.POST['direccion_edit']
	laboratorista.user.save()
	laboratorista.save()

	return redirect('gestion_laboratorista')

def gestion_minsal(request):
	if(request.user.is_authenticated and request.user.rol == 0):
		minsal = Minsal.objects.all()
		contexto = {'minsal': minsal,}
		return render(request, 'gestion_usuarios/gestion_minsal.html', contexto)
	else:
		contexto = {}
		return redirect('/')


def eliminar_minsal(request):

	Minsal.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_minsal')

def registrar_minsal(request):

	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	dui = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 2

	user, minsal = User.objects.get_or_create(
		username = usuario,
		first_name = nombre,
		last_name = apellido,
		email = correo,
		password = password,
		dui = dui,
		direccion = direccion,
		rol = rol,
		is_active = activo,
		is_staff = staff
	)
	
	if minsal:
		user.set_password(password)
		user.save()

	covid_minsal = Minsal()

	covid_minsal.user = user

	covid_minsal.save()

	if request.user.is_authenticated:

		return redirect('gestion_minsal')

	else:
		
		return redirect('/')

def editar_minsal(request):

	minsal = Minsal.objects.get(pk=request.POST['id_edit'])

	minsal.user.first_name = request.POST['nombre_edit']
	minsal.user.last_name = request.POST['apellido_edit']
	minsal.user.username = request.POST['usuario_edit']
	minsal.user.email = request.POST['correo_edit']
	minsal.user.dui = request.POST['telefono_edit']
	minsal.user.direccion = request.POST['direccion_edit']
	minsal.user.save()
	minsal.save()

	return redirect('gestion_minsal')


def gestion_paciente(request):
	if(request.user.is_authenticated and (request.user.rol == 0 or request.user.rol == 1)):
		pacientes = CuadroMedico.objects.all().select_related()
		form = FormFiltrar()
		contexto = {'pacientes': pacientes,'form':form,}
		return render(request, 'gestion_usuarios/gestion_paciente.html', contexto)

	else:
		return redirect('/')	

def registrar_paciente(request):
	nombre_paciente = request.POST['nombre']
	apellido_paciente = request.POST['apellido']
	dui = request.POST['dui']
	sexo = request.POST['sexo']
	d = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
	d.strftime('%Y-%m-%d')

	localidad = Municipio.objects.get(idMunicipio=request.POST['municipio'])

	paciente = Paciente()
	paciente.localidad = localidad
	paciente.nombre_paciente = nombre_paciente
	paciente.apellido_paciente = apellido_paciente
	paciente.dui_paciente = dui
	paciente.sexo_paciente = sexo
	paciente.fecha_paciente = d
	paciente.save()

	cuadro = CuadroMedico()
	cuadro.paciente = paciente
	cuadro.estado_paciente = request.POST['estado']
	cuadro.save()

	if request.user.is_authenticated:

		return redirect('gestion_paciente')

	else:
		
		return redirect('/')


def editar_paciente(request):
	
	paciente = Paciente.objects.get(pk=request.POST['id_edit'])

	paciente.nombre_paciente = request.POST['nombre_edit']
	paciente.apellido_paciente = request.POST['apellido_edit']
	paciente.dui_paciente = request.POST['dui_edit']
	cuadroMedico = CuadroMedico.objects.get(paciente=paciente)
	cuadroMedico.estado_paciente = request.POST['estado_edit']
	paciente.sexo_paciente = request.POST['sexo_edit']
	paciente.fecha_paciente = request.POST['fecha_edit']
	#localidad = Municipio.objects.get(idMunicipio=request.POST['municipio'])
	#paciente.localidad = localidad

	if request.user.rol == 0:
		cuadroMedico.descripcion_paciente = request.POST['sintomas']
	cuadroMedico.save()
	paciente.save()
	return redirect('gestion_paciente')

def caso_sospechoso(request):	
	if(request.user.is_authenticated and request.user.rol == 0):
		cuadros = CuadroMedico.objects.all()
		contexto = {'cuadros': cuadros}
		return render(request, 'expediente/casos-sospechosos.html', contexto)
	else:
		return redirect('/')	

def nexo(request,cuadro_id):
	if(request.user.is_authenticated and request.user.rol == 0):
		cuadros = CuadroMedico.objects.get(pk=cuadro_id)
		casos = CasoSospechoso.objects.filter(cuadro=cuadros)

		contexto = {
			'cuadros':cuadros,
			'casos':casos,
		}

		return render(request, 'expediente/nexos/nexos.html', contexto)
	else:
		return redirect('/')	

def registrar_nexo(request):
	cuadros = CuadroMedico.objects.get(pk=request.POST['cuadro_id'])
	nombre_sospechoso = request.POST['nombre']
	apellido_sospechoso = request.POST['apellido']
	sexo = request.POST['sexo']
	d = datetime.strptime(request.POST['fecha'], '%Y-%m-%d')
	d.strftime('%Y-%m-%d')

	sospechoso = CasoSospechoso()
	sospechoso.nombre_sospechoso = nombre_sospechoso
	sospechoso.apellido_sospechoso = apellido_sospechoso
	sospechoso.sexo_sospechoso = sexo
	sospechoso.fecha_sospechoso = d
	sospechoso.cuadro = cuadros
	sospechoso.save()

	if request.user.is_authenticated:

		return redirect('nexo', cuadro_id=request.POST['cuadro_id'])

	else:
		
		return redirect('/')


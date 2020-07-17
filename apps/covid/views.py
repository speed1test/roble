from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date, datetime
from apps.covid.models import *

import json
from django.http import JsonResponse


from collections import OrderedDict as SortedDict
def index(request):
	return render(request, 'index.html')
def instalaciones(request):
	return render(request, 'menu/Instalaciones.html')
def servicios(request):
	return render(request, 'menu/Servicios.html')
def contacto(request):
	return render(request, 'menu/Contacto.html')
def graficas(request):
	if(request.user.is_authenticated and (request.user.rol == 0 or request.user.rol == 2)):
		return render(request, 'graficas_covid.html')
	else:
		return redirect('/')	
# Create your views here.
def pruebas_resumen(request):
	porResultado =CuadroMedico.objects.all()
	finalrep ={}
	positivo = 0 
	negativo = 0
	for item in porResultado:
		if item.estado_paciente == 1:		
			positivo = positivo + 1
		if item.estado_paciente == 0:
			negativo = negativo + 1

	finalrep["Pacientes Positivos"]=positivo
	finalrep["Pacientes Negativos"]=negativo

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen':finalrep},safe=False)

def pruebas_resumen_genero(request):
	porResultado =CuadroMedico.objects.filter(estado_paciente=1)
	finalrep ={}
	Femenino = 0 
	Masculino = 0
	for item in porResultado:
		if item.paciente.sexo_paciente == 1:		
			Femenino = Femenino + 1
		if item.paciente.sexo_paciente == 0:
			Masculino = Masculino + 1

	finalrep["Femeninos"]=Femenino
	finalrep["Masculinos"]=Masculino

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen_genero':finalrep},safe=False)

def pruebas_resumen_genero_sospechosos(request):
	porResultado =CasoSospechoso.objects.all()
	finalrep ={}
	Femenino = 0 
	Masculino = 0
	for item in porResultado:
		if item.sexo_sospechoso == 1:		
			Femenino = Femenino + 1
		if item.sexo_sospechoso == 0:
			Masculino = Masculino + 1

	finalrep["Femeninos"]=Femenino
	finalrep["Masculinos"]=Masculino

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'pruebas_resumen_genero_sospechosos':finalrep},safe=False)

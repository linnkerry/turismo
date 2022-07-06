from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Incidences, TypeIncidence, TypePerson, Person, Vehiculo, TypeIncidence
from .forms import IncidenciaForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def Login(request):
	return render(request, 'login-acceso.html')

# Create your views here.
def Index(request):
	agente = TypePerson.objects.all()
	contexto = {'agente': agente}
	return render(request, 'index.html',contexto)

def point_datasets(request):
	all_objects = Incidences.objects.all()
	points = serialize('geojson', all_objects)
	return HttpResponse(points,content_type='json')

def Persona(request):
	all_objects = [*Person.objects.all()]
	personas = serialize('json',all_objects)
	return HttpResponse(personas,content_type='json')

def Portal(request):
	incidencias = Person.objects.all()
	vehiculos = Vehiculo.objects.all()
	typeincidence = TypeIncidence.objects.all()
	print(incidencias)
	context = {'incidencias':incidencias,'vehiculos':vehiculos,'typeincidence':typeincidence}
	return render(request, 'portal/index.html', context)


from django.contrib.gis.geos import Point, GEOSGeometry


def Incidencia(request):
	if request.method == "POST":
		persona = Person.objects.get(documento='70033475')
		form = Incidences()
		#post = form.save(commit=False)
		form.agraviado_id = persona.id
		form.agente_id = request.POST['agente_id']
		form.agente_id = request.POST['typeinsidence_id']
		form.typeinsidence_id = request.POST['typeinsidence_id']
		form.vehiculo_id = request.POST['vehiculo_id']
		latitude = request.POST['latitude']
		print(latitude)
		longitude = request.POST['longitude']
		print(longitude)
		form.location = GEOSGeometry('POINT(%s %s), 4326' % (longitude, latitude))
		form.save()
	return redirect("/portal/")

from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

class PersonaViewDetail(APIView):
	def post(self, request, format=None):
		post_data = request.data
		persona = Person.objects.get(documento=post_data['dni'])
		contexto = {'nombre': persona.nombre, 'apepaterno': persona.apepaterno, 'apematerno': persona.apematerno}
		datosJson = json.dumps(contexto, sort_keys=True,
							   indent=1,
							   cls=DjangoJSONEncoder)
		return HttpResponse(datosJson, content_type='application/json')

class CrearPersonaViewDetail(APIView):
	def post(self, request, format=None):
		post_data = request.data
		try:
			persona = Person.objects.get(documento=post_data["dni"])
		except Person.DoesNotExist:
			cp = Person()
			cp.documento = post_data["dni"]
			cp.nombre = post_data["nombres"]
			cp.apepaterno = post_data["apepaterno"]
			cp.apematerno = post_data["apematerno"]
			cp.save()
			pass
		return HttpResponse("success")

from django.shortcuts import render, redirect, get_object_or_404
import json

import requests

class DniNuevoViewDetail(APIView):

	def get_object(self,dni):
		return dni

	def get(self, request, dni, format=None):
		s = requests.Session()
		data=''

		if len(dni) == 8:
			get = s.get("http://digital.regionhuanuco.gob.pe/tramite/persona/dni/"+dni)
			data = get.json()

			if len(data) > 1:
				try:
					persona = Person.objects.get(documento=data["dni"])
				except Person.DoesNotExist:
					cp = Person()
					cp.documento = data["dni"]
					cp.nombre = data["prenombres"]
					cp.apepaterno = data["apPrimer"]
					cp.apematerno = data["apSegundo"]
					cp.save()
					pass
			return Response(data)
		else:
			return Response("Ingrese correctamente su DNI")


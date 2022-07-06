from django.contrib import admin
from .models import Incidences, Person, Radio, TypePerson, TypeIncidence, Vehiculo
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('typeinsidence','location')
admin.site.register(Incidences, IncidencesAdmin)

class RadioAdmin(LeafletGeoAdmin):
	#pass
	list_display =('descripcion','ubicacion')
admin.site.register(Radio, RadioAdmin)

admin.site.register(Person)
admin.site.register(TypePerson)
admin.site.register(TypeIncidence)
admin.site.register(Vehiculo)

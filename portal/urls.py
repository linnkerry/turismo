from django.urls import path
from .views import Index, point_datasets, Portal, Persona, PersonaViewDetail, CrearPersonaViewDetail, Incidencia,Login,DniNuevoViewDetail

urlpatterns = [
	path('',Index, name='index'),
	path('incidence_data/', point_datasets, name='incidences'),
	path('incidencia/', Incidencia, name='incidencia'),
	path('personas_data/', Persona, name='personas'),
	path('portal/', Portal, name='portal'),
	path('login-acceso/', Login, name='login'),

	path('persona/', PersonaViewDetail.as_view()),
	path('crearpersona/', CrearPersonaViewDetail.as_view()),

	path('ubigeo/nuevodni/<str:dni>/',DniNuevoViewDetail.as_view()),
]
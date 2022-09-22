from django.urls import path, include
from Web_Coder import views
urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('Profesores/', views.profesorFormulario, name='profesor' ),
    path('Alumnos/', views.alumnoFormulario, name='alumnos' ),
    path('Materias/', views.materiaFormulario, name='materias' ),
    
]
from django.urls import path
from . import views

app_name='encuesta'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pregunta_id>/',views.detalle,name='detalle'),
    path('suma/<int:n1>/<int:n2>',views.suma,name='suma'),
    path('enviar',views.enviar,name='enviar'),
    path('calculadora',views.calculadora,name='calculadora')
]
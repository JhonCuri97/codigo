from django.shortcuts import render, get_list_or_404

#importar modelso
from .models import Opcion,Pregunta

# Create your views here.
def index(request):
    lista_pregunta= Pregunta.objects.all()
    context={'lstPreguntas': lista_pregunta}
    return render(request,'index.html',context)

def detalle(request,pregunta_id):
    #pregunta= get_list_or_404(Pregunta,pk=pregunta_id)
    pregunta=Pregunta.objects.get(id=pregunta_id)
    print(pregunta.pregunta_texto)
    context={'pregunta':pregunta}
    return render(request,'detalle.html',{'pregunta':pregunta})
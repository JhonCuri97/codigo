from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context={
        'titulo':'Encuesta alumno'
    }
    return render(request,'index.html',context)
    #return HttpResponse("<h2>BIENVENDIO A MI APP DE ENCUESTAS </h2>")

def detalle(request,pregunta_id):
    return HttpResponse("ESTAS VIENDO LA PREGUNTA %s."% pregunta_id)

def suma(request,n1,n2):
    suma=n1+n2
    return HttpResponse("la suma de %s + %s es %s"% (n1,n2,suma))

def enviar(request):
    context={
        'titulo':'respuesta',
        'nombre':request.POST['nombre'],
        'email':request.POST['email'],
        'perfil':request.POST['perfil'],
        'idiomas':request.POST.getlist('idiomas'),
        'github':request.POST['github']
    }
    
    return render(request,'respuesta.html',context)

def calculadora(request):
    context={
        'titulo': 'Respuesta',
        'primer numero': request.POST['n1'],
        'segundo numero': request.POST['n2'],
        'resultado': request.POST['suma']
    }
    
    return render(request,'calculadora.html',context)
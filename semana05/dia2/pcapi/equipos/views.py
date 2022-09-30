from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import EmpleadoSerializer,CargoSerializer
from .models import Empleado,Cargo
# Create your views here.

@api_view()
def index(request):
    return Response({"message": "Hello world!!!"})

@api_view(['GET'])
def empleados(request):
    dataEmpleado=Empleado.objects.all()
    print(dataEmpleado)
    serializer =EmpleadoSerializer(dataEmpleado,many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def crearEmpleado(request):   
    serializer= EmpleadoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    nuevoEmpleado=serializer.save()
    return Response(EmpleadoSerializer(nuevoEmpleado).data) 
    
@api_view(['GET','POST'])
def cargos(request):
    if request.method=='GET': 
        dataCargos= Cargo.objects.all()
        serializer= CargoSerializer(dataCargos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
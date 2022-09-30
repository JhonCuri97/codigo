from rest_framework import viewsets
from .serializers import SerieSerializer
from .models import Serie

# Create your views here.

class SerieViewSet(viewsets.ModelViewSet):
    queryset= Serie.objects.all()
    serializer_class = SerieSerializer


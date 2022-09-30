from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Serie
        fields=('id','nombre','categoria')
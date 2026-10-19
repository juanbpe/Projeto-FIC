from rest_framework import serializers
from apps.cursos.models import Area, PublicoAlvo, Curso

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','nome']

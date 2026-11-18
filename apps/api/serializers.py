from rest_framework import serializers
from apps.cursos.models import Area, PublicoAlvo, Curso
from apps.usuarios.models import Usuario

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','nome']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'username', 'first_name', 'last_name', 'email', 'nascimento']
        read_only_fields = ['cpf']


# aula 05
class UsuarioCadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['cpf', 'username', 'first_name', 'last_name', 'email', 'nascimento', 'password', 'password2']

    def validate_cpf(self, valor):
        if not valor.isdigit() or len(valor) != 11:
            raise serializers.ValidationError('Informe o CPF com 11 números, sem pontos e traço.')
        return valor

    def validate(self, dados):
        if dados['password'] != dados['password2']:
            raise serializers.ValidationError({'password2': 'As senhas não conferem.'})
        return dados

    def create(self, dados):
         dados.pop('password2')
         return Usuario.objects.create_user(**dados)
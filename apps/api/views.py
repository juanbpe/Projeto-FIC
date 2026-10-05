from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.cursos.models import Area, PublicoAlvo, Curso

@api_view(['POST'])
def olamundo(request):
    return Response({'mensagem': 'Olá Mundo!'})

@api_view(['GET'])
def instituicao(request):
    return Response({
        'nome': 'IFRN',
        'campus': 'Cang',
        'cidade': 'Canguaretama',
        'anos': 12
    })

@api_view(['GET'])
def materias(request):
    return Response([
        {'nome': 'Teste', 'ch': 60},
        {'nome': 'Corporativas', 'ch': 120},
        {'nome': 'Implantação', 'ch': 60}
    ])

@api_view(['POST'])
def receber_1(request):
    dados = request.data
    print(dados)
    print(dados['nome'])
    print(dados['disciplina'])
    return Response({'mensagem': 'recebeu'})

@api_view(['GET'])
def areas_lista(request):
    areas = Area.objects.all()
    dados = []
    for area in areas:
        dados.append({'id': area.id, 'nome': area.nome})
    
    return Response(dados)

@api_view(['GET'])
def publico_lista(request):
    publicos = PublicoAlvo.objects.all().order_by()
    dados = []
    for publico in publicos:
        dados.append({'id': publico.id, 'nome': publico.nome})
    
    return Response(dados)
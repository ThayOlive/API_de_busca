from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RelatorioCadop
from .serializers import RelatorioSerializer
from rest_framework import status
from django.db.models import Q

class RegistrosView(APIView):
    def get(self, request, *args, **kwargs):
        dados = RelatorioCadop.objects.all()
        serializer = RelatorioSerializer(dados, many=True)
        return Response(serializer.data)
    
class SeachView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')

        if not query:
            return Response({"erro": "Nenhum termo de busca fornecido"}, status=status.HTTP_400_BAD_REQUEST)
        
        results = RelatorioCadop.objects.filter (
            Q(razao_social__icontains=query) |
            Q(cnpj__icontains=query) |
            Q(registro_ans__icontains=query) |
            Q(nome_fantasia__icontains=query) |
            Q(logradouro__icontains=query) |
            Q(representante__icontains=query) |
            Q(cargo_representante__icontains=query)  
      
        )

        if not results.exists():
            return Response({"message": "Nenhum resultado encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RelatorioSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
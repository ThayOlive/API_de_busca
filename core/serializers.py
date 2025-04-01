from rest_framework import serializers
from .models import RelatorioCadop


class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioCadop
        fields = '__all__'
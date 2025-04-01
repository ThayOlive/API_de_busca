
from django.db import models

class RelatorioCadop(models.Model):
        registro_ans = models.CharField(max_length=10)
        cnpj = models.CharField(unique=True, max_length=14)
        razao_social = models.CharField(max_length=150)
        nome_fantasia = models.CharField(max_length=150, blank=True, null=True)
        modalidade = models.CharField(max_length=100)
        logradouro = models.CharField(max_length=100)
        numero = models.CharField(max_length=20)
        complemento = models.CharField(max_length=50, blank=True, null=True)
        bairro = models.CharField(max_length=50)
        cidade = models.CharField(max_length=50)
        uf = models.CharField(max_length=2)
        cep = models.CharField(max_length=8)
        ddd = models.CharField(max_length=2, blank=True, null=True)
        telefone = models.CharField(max_length=50, blank=True, null=True)
        fax = models.CharField(max_length=15, blank=True, null=True)
        endereco_eletronico = models.CharField(max_length=80, blank=True, null=True)
        representante = models.CharField(max_length=100)
        cargo_representante = models.CharField(max_length=100)
        regiao_de_comercializacao = models.SmallIntegerField(blank=True, null=True)
        data_registro_ans = models.DateField()

        class Meta:
            managed = False
            db_table = 'relatorio_cadop'

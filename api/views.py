from django.shortcuts import render
from api.models import Proprietario, UnidadeHabitacional, GrupoHabitacional, Condominio, TaxaCondominio, ItemTaxa, Despesa, TipoDespesa
from api.serializers import ProprietarioSerializer, UnidadeHabitacionalSerializer, GrupoHabitacionalSerializer, CondominioSerializer, TaxaCondominioSerializer, ItemTaxaSerializer, DespesaSerializer, TipoDespesaSerializer
from rest_framework import authentication, permissions, viewsets

class DefaultsMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ProprietarioViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer


class UnidadeHabitacionalViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = UnidadeHabitacional.objects.all()
    serializer_class = UnidadeHabitacionalSerializer

class GrupoHabitacionalViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = GrupoHabitacional.objects.all()
    serializer_class = GrupoHabitacionalSerializer


class CondominioViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Condominio.objects.all();
    serializer_class = CondominioSerializer



from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'usuario', views.UserViewSet)
router.register(r'proprietario', views.ProprietarioViewSet)
router.register(r'unidade-habitacional', views.UnidadeHabitacionalViewSet)
router.register(r'grupo-habitacional', views.GrupoHabitacionalViewSet)
router.register(r'condominio', views.CondominioViewSet)
router.register(r'taxa-condominio', views.TaxaCondominioViewSet)
router.register(r'item-taxa', views.ItemTaxaViewSet)
router.register(r'despesa', views.DespesaViewSet)
router.register(r'tipo-despesa', views.TipoDespesaViewSet)

urlpatterns =[
    url(r'^', include(router.urls)),
    url(r'^despesa/condominio/(?P<condominio_pk>\d+)/$', views.DespesaViewSet.distribuir_despesa_condominio),
    url(r'^despesa/grupohabitacional/(?P<grupo_habitacional_pk>\d+)/$', views.DespesaViewSet.distribuir_despesa_grupo_habitacional),
    url(r'^despesa/unidadehabitacional/(?P<unidade_habitacional_pk>\d+)/$', views.DespesaViewSet.distribuir_despesa_unidade_habitacional),

]
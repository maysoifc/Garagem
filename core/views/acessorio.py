from rest_framework.viewsets import ModelViewSet
from core.models import Acessorio
from core.seeializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    seeializer_class = AcessorioSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Cor
from core.seeializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serualizer_class = CorSerializer
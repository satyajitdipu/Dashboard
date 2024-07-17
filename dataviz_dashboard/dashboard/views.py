# dashboard/views.py

from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_queryset(self):
        queryset = Data.objects.all()
        sector = self.request.query_params.get('sector', None)
        topic = self.request.query_params.get('topic', None)
        if sector is not None:
            queryset = queryset.filter(sector=sector)
        if topic is not None:
            queryset = queryset.filter(topic=topic)
        return queryset

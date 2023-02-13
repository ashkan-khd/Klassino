from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import State
from user.serializers import StateSerializer, StateAndCitiesSerializer


class StatesListView(mixins.ListModelMixin,
                     GenericViewSet):
    pagination_class = None
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateCitiesView(mixins.RetrieveModelMixin,
                  GenericViewSet):
    pagination_class = None
    queryset = State.objects.all()
    serializer_class = StateAndCitiesSerializer

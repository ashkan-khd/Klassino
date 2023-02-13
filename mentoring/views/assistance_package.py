from django.http import Http404
from rest_framework import viewsets

from mentoring.models import AssistancePackage
from mentoring.serializers.assistance_package import AssistancePackageSerializer


class AssistancePackageView(viewsets.mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = AssistancePackage.active_objects.all()
    serializer_class = AssistancePackageSerializer
    lookup_url_kwarg = 'lookup'

    def get_queryset(self):
        if 'assistant_id' in self.request.query_params:
            return self.queryset.filter(assistant_id=self.request.query_params['assistant_id'])
        else:
            return self.queryset

    def get_object(self):
        lookup = str(self.kwargs['lookup'])

        if lookup.lower() == 'random':
            assistance_package = self.get_queryset().last()
            if assistance_package is None:
                raise Http404
            return assistance_package
        else:
            return super().get_object()


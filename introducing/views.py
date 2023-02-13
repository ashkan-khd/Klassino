from django.http import Http404
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from introducing.serializers import TeacherIntroductionVideoSerializer, AssistantIntroductionVideoSerializer
from user.models import Teacher, Assistant


def has_object_with_id(model, id):
    return model.objects.filter(id=id).exists()


class VideosViewSet(mixins.ListModelMixin,
                    GenericViewSet):

    lookup_url_kwarg = 'user_id'

    def get_serializer_class(self):
        pk = self.kwargs.get(self.lookup_url_kwarg, '-1')
        if has_object_with_id(Teacher, pk):
            return TeacherIntroductionVideoSerializer
        elif has_object_with_id(Assistant, pk):
            return AssistantIntroductionVideoSerializer
        else:
            raise Http404

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg, '-1')
        if has_object_with_id(Teacher, pk):
            return Teacher.objects.get(id=pk).introduction_videos.all()
        elif has_object_with_id(Assistant, pk):
            return Assistant.objects.get(id=pk).introduction_videos.all()
        else:
            raise Http404

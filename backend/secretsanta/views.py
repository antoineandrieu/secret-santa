from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Participant, Blacklist, Draw, DrawParticipant
from .serializers import (
    ParticipantSerializer,
    BlacklistSerializer,
    DrawSerializer,
    DrawParticipantSerializer,
)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class BlacklistViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer


class DrawViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Draw.objects.all()
    serializer_class = DrawSerializer

    @action(detail=False, methods=["post"])
    def create_custom_draw(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            draw = self.perform_create_draw(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create_draw(self, serializer):
        # TODO: Implement logic to create a draw with participants and ensure blacklist constraints
        instance = serializer.save()
        return instance


class DrawParticipantViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = DrawParticipant.objects.all()
    serializer_class = DrawParticipantSerializer

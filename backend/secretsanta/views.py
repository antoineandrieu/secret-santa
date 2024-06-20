import logging

from django.db import transaction
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

logger = logging.getLogger(__name__)


from .models import Participant, Blacklist, Draw, DrawParticipant
from .serializers import (
    ParticipantSerializer,
    BlacklistSerializer,
    DrawSerializer,
    DrawParticipantSerializer,
)
import random


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
    queryset = Draw.objects.all().order_by("-date")
    serializer_class = DrawSerializer

    def list(self, request, *args, **kwargs):
        # Return the last 5 draws
        queryset = self.filter_queryset(self.get_queryset())[:5]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            draw = self.perform_create_draw(serializer)
            return Response(DrawSerializer(draw).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def perform_create_draw(self, serializer):
        draw_instance = serializer.save()

        participants = list(Participant.objects.all())
        random.shuffle(participants)

        # Creating a blacklist map where key is a participant who cannot receive from the values (set of givers)
        blacklist_map = {}
        for entry in Blacklist.objects.all():
            if entry.cannot_receive_from_id not in blacklist_map:
                blacklist_map[entry.cannot_receive_from_id] = set()
            blacklist_map[entry.cannot_receive_from_id].add(entry.participant_id)

        logger.error(f"blacklist_map: {blacklist_map}")

        assignments = {}
        remaining_receivers = set(participants)

        for giver in participants:
            # Exclude the giver from possible receivers and anyone who has blacklisted this giver
            possible_receivers = {
                receiver
                for receiver in remaining_receivers
                if receiver.id != giver.id
                and giver.id not in blacklist_map.get(receiver.id, set())
            }

            if not possible_receivers:
                transaction.set_rollback(True)
                raise ValidationError(
                    f"No valid receivers for participant {giver.name}"
                )

            # Select a receiver
            receiver = random.choice(list(possible_receivers))
            assignments[giver] = receiver
            remaining_receivers.remove(receiver)

        draw_participants = [
            DrawParticipant(draw=draw_instance, giver=giver, receiver=receiver)
            for giver, receiver in assignments.items()
        ]

        DrawParticipant.objects.bulk_create(draw_participants)

        return draw_instance


class DrawParticipantViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = DrawParticipant.objects.all()
    serializer_class = DrawParticipantSerializer

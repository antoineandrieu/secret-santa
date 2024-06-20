from rest_framework import serializers

from .models import Participant, Blacklist, Draw, DrawParticipant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["id", "name", "email"]


class BlacklistSerializer(serializers.ModelSerializer):
    participant = serializers.PrimaryKeyRelatedField(queryset=Participant.objects.all())
    cannot_receive_from = serializers.PrimaryKeyRelatedField(
        queryset=Participant.objects.all()
    )

    class Meta:
        model = Blacklist
        fields = ["id", "participant", "cannot_receive_from"]


class DrawParticipantSerializer(serializers.ModelSerializer):
    giver = ParticipantSerializer(read_only=True)
    receiver = ParticipantSerializer(read_only=True)

    class Meta:
        model = DrawParticipant
        fields = ["id", "giver", "receiver"]


class DrawSerializer(serializers.ModelSerializer):
    participants = DrawParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Draw
        fields = ["id", "date", "participants"]

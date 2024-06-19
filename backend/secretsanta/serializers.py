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


class DrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draw
        fields = ["id", "date"]


class DrawParticipantSerializer(serializers.ModelSerializer):
    draw = serializers.PrimaryKeyRelatedField(queryset=Draw.objects.all())
    giver = serializers.SlugRelatedField(
        slug_field="name", queryset=Participant.objects.all()
    )
    receiver = serializers.SlugRelatedField(
        slug_field="name", queryset=Participant.objects.all()
    )

    class Meta:
        model = DrawParticipant
        fields = ["id", "draw", "giver", "receiver"]

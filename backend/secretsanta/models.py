from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Blacklist(models.Model):
    participant = models.ForeignKey(
        Participant, related_name="blacklisting", on_delete=models.CASCADE
    )
    cannot_receive_from = models.ForeignKey(
        Participant, related_name="blocked_by", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("participant", "cannot_receive_from")

    def __str__(self):
        return f"{self.participant.name} cannot receive gifts from {self.cannot_receive_from.name}"


class Draw(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Draw on {self.date.strftime('%Y-%m-%d %H:%M')}"


class DrawParticipant(models.Model):
    draw = models.ForeignKey(
        Draw, related_name="participants", on_delete=models.CASCADE
    )
    giver = models.ForeignKey(
        Participant, related_name="giving", on_delete=models.PROTECT
    )
    receiver = models.ForeignKey(
        Participant, related_name="receiving", on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ("draw", "giver", "receiver")

    def __str__(self):
        return f"{self.giver.name} gives a gift to {self.receiver.name}"

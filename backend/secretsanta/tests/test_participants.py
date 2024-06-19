from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from secretsanta.models import Participant


class ParticipantAPITests(APITestCase):
    def test_create_participant(self):
        url = reverse("participant-list")
        data = {"name": "John", "email": "john@example.com"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Participant.objects.count(), 1)
        self.assertEqual(Participant.objects.get().name, "John")

    def test_read_participants(self):
        Participant.objects.create(name="Jane", email="jane@example.com")
        url = reverse("participant-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_participant_with_duplicate_email(self):
        Participant.objects.create(name="Alice", email="alice@example.com")
        url = reverse("participant-list")
        data = {"name": "Alice", "email": "alice@example.com"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Participant.objects.count(), 1)

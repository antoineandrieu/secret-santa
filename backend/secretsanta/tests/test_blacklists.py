from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from secretsanta.models import Participant, Blacklist


class BlacklistAPITests(APITestCase):
    def setUp(self):
        self.participant1 = Participant.objects.create(
            name="Alice", email="alice@example.com"
        )
        self.participant2 = Participant.objects.create(
            name="Bob", email="bob@example.com"
        )

    def test_create_blacklist(self):
        url = reverse("blacklist-list")
        data = {
            "participant": self.participant1.id,
            "cannot_receive_from": self.participant2.id,
        }
        print(data)
        response = self.client.post(url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blacklist.objects.count(), 1)

    def test_delete_blacklist(self):
        blacklist = Blacklist.objects.create(
            participant=self.participant1, cannot_receive_from=self.participant2
        )
        url = reverse("blacklist-detail", args=[blacklist.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Blacklist.objects.count(), 0)

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
        response = self.client.post(url, data, format="json")
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

    def test_get_blacklist(self):
        Blacklist.objects.create(
            participant=self.participant1, cannot_receive_from=self.participant2
        )
        url = reverse("blacklist-list") + f"?participant={self.participant1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["participant"], self.participant1.id)
        self.assertEqual(response.data[0]["cannot_receive_from"], self.participant2.id)

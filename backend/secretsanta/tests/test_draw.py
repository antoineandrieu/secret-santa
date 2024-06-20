from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from secretsanta.models import Participant, Blacklist


class DrawTestCase(TestCase):

    def setUp(self):
        super().setUp()

        # Load data directly to check what's being inserted
        call_command("loaddata", "participants.json")
        call_command("loaddata", "blacklists.json")

        self.client = APIClient()

        # Check that there are exactly 4 participants with IDs 1, 2, 3, 4
        expected_participant_ids = {1, 2, 3, 4}
        actual_participant_ids = set(Participant.objects.values_list("id", flat=True))
        if expected_participant_ids != actual_participant_ids:
            raise ValueError(
                f"Expected participant IDs {expected_participant_ids}, but found {actual_participant_ids}"
            )

        # Check that there are exactly 8 blacklist entries
        expected_blacklist_count = 8
        actual_blacklist_count = Blacklist.objects.count()
        if actual_blacklist_count != expected_blacklist_count:
            raise ValueError(
                f"Expected {expected_blacklist_count} blacklist entries, found {actual_blacklist_count}"
            )

    def test_draw(self):
        # Simulate the POST request to create a draw
        response = self.client.post(
            reverse("draw-list")
        )  # Use the correct endpoint name
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Fetch the created draw details
        draw_data = response.json()

        # Extract givers and receivers
        givers = {
            participant["giver"]["id"] for participant in draw_data["participants"]
        }
        receivers = {
            participant["receiver"]["id"] for participant in draw_data["participants"]
        }

        # Check for unique givers and receivers
        self.assertEqual(len(givers), 4, "There should be exactly 4 unique givers")
        self.assertEqual(
            len(receivers), 4, "There should be exactly 4 unique receivers"
        )

        # Validate against the two valid possibilities using sets of frozensets
        valid_combination_1 = {
            frozenset({1, 2}),
            frozenset({2, 3}),
            frozenset({3, 4}),
            frozenset({4, 1}),
        }
        valid_combination_2 = {
            frozenset({4, 1}),
            frozenset({1, 2}),
            frozenset({3, 4}),
            frozenset({2, 3}),
        }

        current_combination = {
            frozenset({participant["giver"]["id"], participant["receiver"]["id"]})
            for participant in draw_data["participants"]
        }

        self.assertTrue(
            current_combination == valid_combination_1
            or current_combination == valid_combination_2,
            "The pairing should match one of the two valid combinations",
        )

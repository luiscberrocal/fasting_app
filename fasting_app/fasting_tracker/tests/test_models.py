from datetime import timedelta

from django.test import TestCase

from fasting_app.fasting_tracker.models import FastingSession
from fasting_app.users.tests.factories import UserFactory

from django.utils import timezone


class TestFastingSession(TestCase):
    def test_longest_fasting_session(self):
        user = UserFactory.create()
        start_date = timezone.now()
        end_date = start_date + timedelta(hours=5)
        attributes = {"user": user, "start_date": start_date, "end_date": end_date}
        session = FastingSession(**attributes)
        session.save()
        longest_session = FastingSession.objects.longest_fasting_session(user=user)
        self.assertEquals(longest_session.user, user)

from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Avengers', universe='Marvel')
        self.user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Avengers')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Tony Stark')

    def test_activity_str(self):
        self.assertIn('Tony Stark', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')

    def test_leaderboard_str(self):
        self.assertIn('Tony Stark', str(self.leaderboard))

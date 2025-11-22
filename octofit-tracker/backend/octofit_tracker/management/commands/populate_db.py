from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        db.users.create_index([("email", 1)], unique=True)

        # Insert users
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
            {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "marvel"},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
            {"name": "dc", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"user": "superman@dc.com", "activity": "flying", "duration": 60},
            {"user": "batman@dc.com", "activity": "martial arts", "duration": 45},
            {"user": "ironman@marvel.com", "activity": "flight suit training", "duration": 50},
        ]
        db.activities.insert_many(activities)

        # Insert workouts
        workouts = [
            {"user": "cap@marvel.com", "workout": "shield throw", "reps": 100},
            {"user": "widow@marvel.com", "workout": "acrobatics", "reps": 80},
            {"user": "wonderwoman@dc.com", "workout": "lasso practice", "reps": 70},
        ]
        db.workouts.insert_many(workouts)

        # Insert leaderboard
        leaderboard = [
            {"team": "marvel", "points": 250},
            {"team": "dc", "points": 230},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

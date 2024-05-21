from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"Username: {self.username} Email: {self.email}"

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coach")
    full_name = models.CharField(max_length=100)
    trainer_for = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.full_name

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    training_for = models.TextField()

    def __str__(self):
        return self.full_name

class TrainingSession(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.FloatField()

    def __str__(self):
        return f"{self.coach.full_name} - {self.athlete.full_name}"

class Review(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.coach.full_name} by {self.athlete.full}"
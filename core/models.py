from django.db import models
from django.contrib.auth.models import User
import uuid  #unique id

class PasswordReset(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)   #unique id will be generated
    created_when=models.DateTimeField(auto_now_add=True)                         #time stamp which is 10mins after which id resets

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"   


class Athlete(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sport = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    speed = models.FloatField(null=True, blank=True)     # optional for future use
    stamina = models.FloatField(null=True, blank=True)   # optional for future use

    def __str__(self):
        return f"{self.name} - {self.sport}"


class Interaction(models.Model):
    scout = models.ForeignKey(User, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    action = models.CharField(max_length=20)  # e.g., 'shortlisted'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scout.username} {self.action} {self.athlete.name}"
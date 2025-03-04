from django.db import models
from django.contrib.auth.models import User
import uuid  #unique id

class PasswordReset(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)   #unique id will be generated
    created_when=models.DateTimeField(auto_now_add=True)                         #time stamp which is 10mins after which id resets

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"   



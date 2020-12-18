from django.db import models
from django.contrib.auth import get_user_model

# Create model here
class Question(models.Model):
  topic = models.CharField(max_length=100)
  content = models.CharField(max_length=500)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
      return f"Question topic is '{self.topic}' the Question is {self.content}."

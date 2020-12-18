from django.db import models
from django.contrib.auth import get_user_model

# Create model here
class Answer(models.Model):
    answer_title = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Answer title is '{self.answer_title}' answer content is {self.answer}."

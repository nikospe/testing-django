from django.db import models
from django.utils.timezone import now

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    date = models.DateField(default=now())

    def to_json(self):
        return {
            'id': self.id,
            'text': self.text
        }

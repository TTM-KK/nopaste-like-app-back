from django.db import models

# Create your models here.


class TextData(models.Model):
    text = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        return str(self.id)

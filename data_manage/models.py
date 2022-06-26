from django.db import models

# Create your models here.


class TextData(models.Model):
    text = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True)
    lang = models.CharField(max_length=15 ,blank=True)

    def __str__(self):
        return str(self.id)

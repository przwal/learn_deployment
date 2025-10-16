from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.name


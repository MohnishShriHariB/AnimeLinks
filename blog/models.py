from django.db import models


class blog1(models.Model):
    title=models.CharField(max_length=100)
    disc=models.TextField()
    date = models.DateTimeField()
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title

from django.db import models

class project(models.Model):
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio_1/images/')
    url1=models.URLField(blank=True)
    def __str__(self):
        return self.title
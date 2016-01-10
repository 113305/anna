from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=100)
    created_year = models.IntegerField()
    materials = models.CharField(max_length=100)
    size_height = models.IntegerField()
    size_width = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.title

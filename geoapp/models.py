from django.db import models

# Create your models here.


class Grid(models.Model):
    points = models.CharField(max_length=1000)
    closest_points = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.points} - {self.closest_points}" 
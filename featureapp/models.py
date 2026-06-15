from django.db import models

# Create your models here.


class FeatureModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
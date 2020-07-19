from django.db import models


class SDG(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models


class Zipcode(models.Model):
    zipcode = models.PositiveIntegerField()

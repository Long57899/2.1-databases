from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150, null=False)
    price = models.IntegerField()
    image = models.CharField(max_length = 300)
    release = models.DateField()
    lte_exists = models.CharField(max_length = 6, default = '-' )
    slug = models.SlugField(max_length=200)











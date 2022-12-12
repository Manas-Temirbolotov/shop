from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.name

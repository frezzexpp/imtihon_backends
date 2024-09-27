from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    manufacture = models.TextField()
    cat = models.ForeignKey("Category", models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
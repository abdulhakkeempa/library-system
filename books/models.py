from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=256, null=False)

class Tags(models.Model):
    genre = models.CharField(max_length=100, null=False)

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    author = models.ManyToManyField(Author)
    stock = models.IntegerField(null=False)
    genre = models.ManyToManyField(Tags)
    per_day_charge = models.IntegerField(null=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
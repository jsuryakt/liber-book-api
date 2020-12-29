from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    description = models.TextField()
    book_cover = models.URLField(max_length = 500)
    book_link = models.URLField(max_length = 500)

    def __str__(self):
        return self.name
        
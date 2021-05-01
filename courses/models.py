from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=70)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.IntegerField()

    def __str__(self):
        return self.name

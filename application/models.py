from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to = 'student_images/', blank=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=20)


    def __str__(self):
        return self.name
    
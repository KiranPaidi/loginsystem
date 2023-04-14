from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name
class Course(models.Model):
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=50)
    city_name = models.ForeignKey(City,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)


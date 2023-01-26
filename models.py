from django.db import models

# Create your models here.
class City(models.Model):
    City_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.City_Name}"

class Course(models.Model):
    Course_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Course_Name}"

class Student(models.Model):
    Stud_Name = models.CharField(max_length=50)
    Stud_Age = models.IntegerField()
    Stud_Phone = models.BigIntegerField()
    Stud_City = models.ForeignKey(City,on_delete=models.CASCADE)
    Stud_Course = models.ForeignKey(Course,on_delete=models.CASCADE)
from django.db import models

# Create your models here.

from django.db import models

class EmployeeModel(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='employees/')

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


 
class Address(models.Model):
    city = models.CharField(max_length = 50)


class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT) 



class Card(models.Model):
    card_number = models.IntegerField()
    
    def __str__(self):
     return str(self.card_number)
    
    
class Department(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length = 50)
    code = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} ({self.code})" 
    
class Students(models.Model):
     name = models.CharField(max_length = 50)
     card = models.OneToOneField(Card, on_delete=models.PROTECT)
     department = models.ForeignKey(Department, on_delete=models.CASCADE)
     course = models.ManyToManyField(Course)

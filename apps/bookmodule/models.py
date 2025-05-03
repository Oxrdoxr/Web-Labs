from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Card(models.Model):
    card_Num = models.IntegerField()

    def __str__(self):
        return str(self.card_Num)

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students', null=True)
    course = models.ManyToManyField(Course, related_name='students', blank=True)


    def __str__(self):
        return self.name
    
class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ManyToManyField(Address2)  # هنا ManyToMany بدل ForeignKey

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
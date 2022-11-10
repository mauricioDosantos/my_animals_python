from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    breed = models.CharField(max_length=250, blank=True, null=True)
    weight = models.FloatField()
    height = models.FloatField()
    people_id = models.ForeignKey('people.People', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VaccineCard(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    animals = models.ManyToManyField("Animal", verbose_name="animals")
    vaccines = models.ManyToManyField("Vaccine", verbose_name="vaccines")

    def __str__(self):
        return self.animals.name


class Vaccine(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    dose = models.CharField(max_length=250, blank=True, null=True)
    days_between_dose = models.IntegerField()
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class TaskList(models.Model):
    ref_date = models.DateTimeField(blank=True, null=True)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE, null=True)
    tasks = models.ManyToManyField("Task", verbose_name="tasks")

    def __str__(self):
        return
        names = ', '.join([i for i in self.animals.name])
        return names


class Task(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    ref_date = models.DateTimeField(blank=True, null=True)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", verbose_name="products")

    def __str__(self):
        return
    

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User


class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} | {self.user.email}'
    


class Address(models.Model):
    zip_code = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    complement = models.CharField(max_length=250, blank=True, null=True)
    district = models.CharField(max_length=250, blank=True, null=True)
    number = models.FloatField()
    people_id = models.ForeignKey('People', on_delete=models.CASCADE)

    def __str__(self):
        return self.people_id.user.username


class MyPlan(models.Model):
    animal_quantity = models.IntegerField()
    surplus_value = models.FloatField()
    people_id = models.ForeignKey('People', on_delete=models.CASCADE)
    plan_id = models.ForeignKey('Plan', related_name='plan', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.people_id.user.username} | {self.plan_id.name}'


class Plan(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    value = models.FloatField()
    animal_limit = models.IntegerField()
    surplus_per_animal = models.FloatField()

    def __str__(self):
        return self.name
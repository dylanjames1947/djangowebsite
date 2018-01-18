from django.db import models
from django.urls import reverse


class Organization(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' : ' + self.email + ' : ' + self.password


class Company(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' : ' + self.location


def get_absoulute_url():
    return reverse('register:contracts', kwargs={})


class Contracts(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    value = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    period_of_work = models.CharField(max_length=500)
    bid_opening_date = models.CharField(max_length=500)
    bid_closing_date = models.CharField(max_length=500)
    current_bid = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' : ' + self.description + ' : ' + self.location + ' : ' + self.value + ' : ' + self.category + ' : ' + self.period_of_work


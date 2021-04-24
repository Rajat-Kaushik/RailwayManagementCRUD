from django.db import models
from django.urls import reverse
from django import forms


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()

    travelDate = models.DateField()
    source = models.TextField()
    dest = models.TextField()

    train = models.TextField()
    price = models.FloatField()

    intTravel = models.BooleanField()
    setuStatus = models.CharField(max_length=50)
    report = models.BooleanField()
   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ticketCRUD:ticket_edit', kwargs={'pk': self.pk})
    

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ticket
from django.shortcuts import render

def index(request):
    return render(request,'ticketCRUD/index.html')


class TicketList(ListView):
    model = Ticket

class TicketCreate(CreateView):
    model = Ticket
    fields = ['name', 'age','address','city','state','travelDate','source','dest','train','price','intTravel','setuStatus','report']
    success_url = reverse_lazy('ticketCRUD:ticket_list')

class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['name', 'age','address','city','state','travelDate','source','dest','train','price','intTravel','setuStatus','report']
    success_url = reverse_lazy('ticketCRUD:ticket_list')

class TicketDelete(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticketCRUD:ticket_list')
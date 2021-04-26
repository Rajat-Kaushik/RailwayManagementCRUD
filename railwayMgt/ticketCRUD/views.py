from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ticket
from django.shortcuts import render


class Index(TemplateView):
    template_name = 'ticketCRUD/index.html'


class TicketList(ListView):
    model = Ticket
    template_name = 'ticketCRUD/ticket_list.html'

class TicketCreate(CreateView):
    model = Ticket
    fields = ['name', 'age','address','city','state','travelDate','source','dest','train','price','intTravel','setuStatus','report','image']
    template_name = 'ticketCRUD/ticket_form.html'
    success_url = reverse_lazy('ticketCRUD:ticket_list')

class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['name', 'age','address','city','state','travelDate','source','dest','train','price','intTravel','setuStatus','report','image']
    template_name = 'ticketCRUD/ticket_edit.html'
    success_url = reverse_lazy('ticketCRUD:ticket_list')


class TicketDelete(DeleteView):
    model = Ticket
    template_name = 'ticketCRUD/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticketCRUD:ticket_list')
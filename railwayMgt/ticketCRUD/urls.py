from django.urls import path
from . import views

app_name = 'ticketCRUD'

urlpatterns = [
  path('', views.index, name='index'),
  path('tickets', views.TicketList.as_view(), name='ticket_list'),
  path('new/', views.TicketCreate.as_view(), name='ticket_new'),
  path('edit/<int:pk>/', views.TicketUpdate.as_view(), name='ticket_edit'),
  path('delete/<int:pk>/', views.TicketDelete.as_view(), name='ticket_delete'),
]
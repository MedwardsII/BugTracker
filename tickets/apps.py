#apps module
from django.apps import AppConfig


class TicketConfig(AppConfig):
    '''Ticket configuration class'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickets'

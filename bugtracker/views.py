from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Project, Ticket, TicketAssignment


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def dashboard(request):
    data = {
        'page_name': 'Dashboard',
        'tickets': Ticket.objects.all(),
        'projects': Project.objects.all(),
        'ticket_assignments': TicketAssignment
    }
    return render(request, 'dashboard.html', data)
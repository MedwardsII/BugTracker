'''Module of functions to assist in additional view operations'''
from .models import TicketAssignment


def populate_viewed_tickets(request, ticket):
    '''Populates recentaly viewed ticket list'''
    max_viewed_tickets_length = 10
    viewed_tickets = request.session.get('viewed_tickets', [])
    viewed_ticket = [ticket.pk, ticket.title]

    if viewed_ticket in viewed_tickets:
        viewed_tickets.pop(viewed_tickets.index(viewed_ticket))

    viewed_tickets.insert(0, viewed_ticket)
    viewed_tickets = viewed_tickets[:max_viewed_tickets_length]
    request.session['viewed_tickets'] = viewed_tickets

def change_ticket_assignment(ticket, assignment_form):
    '''Change assigned user of a ticket'''
    ticket_assignment = TicketAssignment.objects.filter(ticket=ticket)
    ticket_assignment.update_or_create(
        assigned_user=assignment_form.cleaned_data['assigned_user'],
        ticket=ticket
    )


def post_comment(ticket, comment_form, user):
    '''Create comment'''
    comment_form.instance.ticket = ticket
    comment_form.instance.creator = user
    if comment_form.is_valid():
        comment_form.save()

def destroy_assignment(ticket):
    '''Destroys a ticket assignment'''
    TicketAssignment.objects.filter(ticket=ticket).delete()

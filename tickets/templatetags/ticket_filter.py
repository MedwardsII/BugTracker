from django import template
from django.contrib.auth.models import User
from django.db.models import F
from tickets.models import TicketComment


register = template.Library()

@register.filter(name='has_perm_assignment')
def has_perm_assignment(user):
    '''Return true if user has permision
    to change assignment of a ticket'''
    return user.has_perm('change_ticket_assignment')

@register.filter(name='assigned_user')
def assigned_user(ticket):
    '''Return User assigned to ticket'''
    assigned_user = User.objects.filter(ticketassignment__ticket=ticket)
    return assigned_user[0] if assigned_user else "Pending"

@register.filter(name='get_comments')
def get_comments(ticket):
    '''Gets comments made on ticket.'''
    comments = TicketComment.objects.filter(ticket=ticket).order_by('-created_on')
    return comments if comments else None

@register.filter(name='tickets_not_complete')
def tickets_not_complete(tickets):
    '''Returns number of tickets not complete.'''
    return len(tickets.filter(is_resolved='No'))

@register.filter(name='tickets_pending_assignment')
def tickets_pending_assignment(tickets):
    '''Returns number of tickets pending assignment'''
    return len(tickets.exclude(is_resolved='Yes').exclude(ticketassignment__ticket=F('pk')))

@register.filter(name='complete_ticket_diff')
def complete_ticket_diff(tickets):
    '''Misc func for styling total tickets pending'''
    complete = tickets.filter(is_resolved='Yes')
    return complete.count() // tickets.count() 

@register.filter(name='tickets_assigned')
def tickets_assigned(tickets, user):
    '''Returns number of tickets assigned to user'''
    return len(tickets.filter(ticketassignment__assigned_user=user))

@register.filter(name='page_name')
def page_name(path):
    '''Returns the page name'''
    page_name = path.split('/')
    if 'update' in page_name:
        return page_name[3].capitalize()
    elif 'comment' in page_name:
        return page_name[4].capitalize()
    else:
        return page_name[2].capitalize()

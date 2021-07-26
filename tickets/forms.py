'''forms module'''
from django import forms
from .models import Ticket, TicketComment, TicketAssignment


class TicketForm(forms.ModelForm):
    '''TicketForm class'''
    class Meta:
        '''TicketForm meta class'''
        model = Ticket
        fields = [
            'title',
            'description',
            'request_type',
            'priority',
            'project'
        ]

class TicketEditForm(forms.ModelForm):
    '''TicketEditForm class'''
    class Meta:
        '''TicketEditForm meta class'''
        model = Ticket
        fields = [
            'request_type',
            'is_resolved',
            'priority'
        ]

class TicketCommentForm(forms.ModelForm):
    '''TicketCommentForm class'''
    class Meta:
        '''TicketCommentForm meta class'''
        model = TicketComment
        fields = ['comment']

class TicketAssignmentForm(forms.ModelForm):
    '''TicketAssignmentForm class'''
    class Meta:
        '''TicketAssignmentForm meta class'''
        model = TicketAssignment
        fields = [
            'assigned_user',
        ]

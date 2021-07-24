from django import forms
from .models import Ticket, TicketComment, TicketAssignment
from django.forms.models import inlineformset_factory


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'request_type',
            'priority',
            'project'
        ]

class TicketEditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'request_type',
            'is_resolved',
            'priority'
        ]

class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['comment']

class TicketAssignmentForm(forms.ModelForm):
    class Meta:
        model = TicketAssignment
        fields = [
            'assigned_user',
        ]

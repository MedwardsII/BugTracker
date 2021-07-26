'''Models Module'''
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    '''Project class model'''
    title = models.CharField(
        max_length=50
    )

    def __str__(self):
        return str(self.title)


class Ticket(models.Model):
    '''Ticket class model'''
    class PriorityLevel(models.TextChoices):
        '''Priority level class'''
        LOW = 'Low'
        URGENT = 'Urgent'
        CRITICAL = 'Critical'

    class ResolutionText(models.TextChoices):
        '''Resolution text class'''
        YES = 'Yes'
        NO = 'No'

    class RequestType(models.TextChoices):
        '''Request type class'''
        BUG = 'Bug'
        RECOMMEND = 'Recommend'
        HELP = 'Help'

    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        help_text='Detailed description of request.'
    )
    request_type = models.CharField(
        max_length=9,
        choices=RequestType.choices,
        default=RequestType.BUG
    )
    is_resolved = models.CharField(
        'Resolved',
        max_length=3,
        choices=ResolutionText.choices,
        default=ResolutionText.NO,
    )
    priority = models.CharField(
        max_length=8,
        choices=PriorityLevel.choices,
        default=PriorityLevel.LOW,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Date ticket was created.'
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text='Date ticket was last modified.'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        help_text="The project this ticket is associated with."
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.title)


class TicketComment(models.Model):
    '''Ticket comment model class'''
    comment = models.TextField(
        max_length=500
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Date ticket was created.'
    )


class TicketAssignment(models.Model):
    '''Ticket assignment class model'''
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE
    )

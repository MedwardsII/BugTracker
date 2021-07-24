from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length=50
    )
    def __str__(self):
        return self.title

class Ticket(models.Model):
    class PriorityLevel(models.TextChoices):
        LOW = 'Low'
        URGENT = 'Urgent'
        CRITICAL = 'Critical'
    class ResolutionText(models.TextChoices):
        YES = 'Yes',
        NO = 'No'
    class RequestType(models.TextChoices):
        BUG = 'Bug',
        RECOMMEND = 'Recommend',
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
        on_delete=CASCADE
    )
    def __str__(self):
        return self.title

class TicketComment(models.Model):
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
    assigned_user = models.ForeignKey(
        User,
        on_delete=CASCADE
    )
    ticket = models.OneToOneField(
        Ticket,
        on_delete=CASCADE
    )
from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from tickets import models
from tickets.models import Ticket, Project, TicketComment, TicketAssignment
from django.contrib.auth.models import User
from rest_framework.exceptions import NotAuthenticated, PermissionDenied


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'request_type',
            'is_resolved',
            'priority',
            'created_on',
            'last_updated',
            'project',
            'creator',
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title']

class TicketAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAssignment
        fields = [
            'ticket',
            'assigned_user'
        ]

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = [
            'comment',
            'creator',
            'ticket',
            'created_on'
        ]
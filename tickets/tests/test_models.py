from time import time
from django.contrib.auth import authenticate
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import response
from tickets.models import Ticket, Project, TicketComment, TicketAssignment


class TestProjectModel(TestCase):
    '''Test the ticket model.'''
    def setUp(self):
        self.project = Project(title='Project test')
    def test_create_project(self):
        self.assertIsInstance(self.project, Project)
    def test_str_representation(self):
        self.assertEquals(str(self.project), 'Project test')

class TestTicketModel(TestCase):
    def setUp(self):
        self.test_user = User(username='Test User', email='test@testmail.net')
        self.project = Project(title='Project test')
        self.ticket = Ticket(
            title='Title test',
            description='Description test',
            request_type='BUG',
            is_resolved='NO',
            priority='LOW',
            created_on=time(),
            last_updated=time(),
            project=self.project,
            creator=self.test_user
        )
    def test_create_ticket(self):
        self.assertIsInstance(self.ticket, Ticket)
    def test_str_representation(self):
        self.assertEquals(str(self.ticket), 'Title test')

class TestTicketCommentModel(TestCase):
    def setUp(self):
        self.test_user = User(username='Test User', email='test@testmail.net')
        self.project = Project(title='Project test')
        self.ticket = Ticket(
            title='Title test',
            description='Description test',
            request_type='BUG',
            is_resolved='NO',
            priority='LOW',
            created_on=time(),
            last_updated=time(),
            project=self.project,
            creator=self.test_user
        )
        self.comment = TicketComment(
            comment='Test comment.',
            creator=self.test_user,
            ticket=self.ticket,
            created_on=time()
        )

class TestTicketAssignmentModel(TestCase):
    def setUp(self):
        self.test_user = User(username='Test User', email='test@testmail.net')
        self.project = Project(title='Project test')
        self.ticket = Ticket(
            title='Title test',
            description='Description test',
            project=self.project,
        )
        self.assignment = TicketAssignment(
            assigned_user=self.test_user,
            ticket=self.ticket
        )
    def test_create_ticket_assignment(self):
        self.assertIsInstance(self.assignment, TicketAssignment)

'''Test module for models'''
from time import time
from django.test import TestCase
from django.contrib.auth.models import User
from tickets.models import Ticket, Project, TicketComment, TicketAssignment


class TestProjectModel(TestCase):
    '''Test the project model.'''
    def setUp(self):
        self.project = Project(title='Project test')
    def test_create_project(self):
        self.assertIsInstance(self.project, Project)
    def test_str_representation(self):
        self.assertEquals(str(self.project), 'Project test')

class TestTicketModel(TestCase):
    '''Test the ticket model.'''
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
    '''Test the ticket comment model.'''
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
    '''Test the assignment model.'''
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

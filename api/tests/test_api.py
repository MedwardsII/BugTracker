from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from tickets.models import Ticket, Project, TicketAssignment, TicketComment
from api.views import TicketViewSet, ProjectViewSet, TicketCommentViewSet, \
    TicketAssignmentViewSet, UserViewSet


class TestUserApi(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.factory = APIRequestFactory()
    def test_get_users(self):
        response = UserViewSet()
        self.assertEqual(response.queryset[0], self.test_user)

class TestTicketsApi(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        project = Project.objects.create(title="Project test")
        self.ticket = Ticket.objects.create(
            title='Title test',
            description='Description test',
            project=project,
            creator=self.test_user
        )
        self.factory = APIRequestFactory()
    def test_get_tickets(self):
        response = TicketViewSet()
        self.assertEqual(response.queryset[0], self.ticket)
    def test_post_tickets(self):
        pass

class TestProjectApi(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.project = Project.objects.create(title="Project test")
        self.factory = APIRequestFactory()
    def test_get_projects(self):
        response = ProjectViewSet()
        self.assertEqual(response.queryset[0], self.project)

class TestCommentsApi(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        project = Project.objects.create(title="Project test")
        self.ticket = Ticket.objects.create(
            title='Title test',
            description='Description test',
            project=project,
            creator=self.test_user
        )
        self.comment = TicketComment.objects.create(
            comment='Test comment',
            creator=self.test_user,
            ticket=self.ticket
        )
        self.factory = APIRequestFactory()
    def test_get_comments(self):
        response = TicketCommentViewSet()
        self.assertEqual(response.queryset[0], self.comment)

class TestAssignmentsApi(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        project = Project.objects.create(title="Project test")
        self.ticket = Ticket.objects.create(
            title='Title test',
            description='Description test',
            project=project,
            creator=self.test_user
        )
        self.assignment = TicketAssignment.objects.create(
            assigned_user=self.test_user,
            ticket=self.ticket
        )
        self.factory = APIRequestFactory()
    def test_get_comments(self):
        response = TicketAssignmentViewSet()
        self.assertEqual(response.queryset[0], self.assignment)
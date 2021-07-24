from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from tickets.models import Ticket, Project
from django.contrib.sessions.middleware import SessionMiddleware
from tickets.views import CommentCreateView, TicketListView, TicketResolvedListView, \
    TicketCreateView, TicketDetailView, TicketUpdateView


class TestTicketListView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        self.factory = RequestFactory()
    def test_ticket_list_view_not_authenticated(self):
        request = self.factory.get('tickets:list_all')
        request.user = AnonymousUser()
        response = TicketListView.as_view()(request)
        self.assertEquals(response.status_code, 302)
    def test_ticket_list_view_authenticated(self):
        request = self.factory.get('tickets:list_all')
        request.user = self.test_user
        response = TicketListView.as_view()(request)
        self.assertEquals(response.status_code, 200)

class TestTicketDetailView(TestCase):
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
        self.factory = RequestFactory()
        self.middleware = SessionMiddleware()
    def test_ticket_detail_view_get_not_authenticated(self):
        request = self.factory.get('tickets:details')
        request.user = AnonymousUser()
        self.middleware.process_request(request)
        response = TicketDetailView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 302)
    def test_ticket_detail_view_get_authenticated(self):
        request = self.factory.get('tickets:details')
        request.user = self.test_user
        self.middleware.process_request(request)
        response = TicketDetailView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 200)

class TestTicketArchivedView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        self.factory = RequestFactory()
    def test_ticket_list_view_not_authenticated(self):
        request = self.factory.get('tickets:list_resolved')
        request.user = AnonymousUser()
        response = TicketResolvedListView.as_view()(request)
        self.assertEquals(response.status_code, 302)
    def test_ticket_list_view_authenticated(self):
        request = self.factory.get('tickets:list_resolved')
        request.user = self.test_user
        response = TicketResolvedListView.as_view()(request)
        self.assertEquals(response.status_code, 200)

class TestTicketCreateView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        self.factory = RequestFactory()
    def test_ticket_create_view_get_not_authenticated(self):
        request = self.factory.get('tickets:create_ticket')
        request.user = AnonymousUser()
        response = TicketCreateView.as_view()(request)
        self.assertEquals(response.status_code, 302)
    def test_ticket_create_view_get_authenticated(self):
        request = self.factory.get('tickets:create_ticket')
        request.user = self.test_user
        response = TicketCreateView.as_view()(request)
        self.assertEquals(response.status_code, 200)
    def test_ticket_create_view_post_authenticated(self):
        request = self.factory.post('tickets:create_ticket')
        request.user = self.test_user
        response = TicketCreateView.as_view()(request)
        self.assertEquals(response.status_code, 200)
    
class TestTicketCommentCreateView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        project = Project.objects.create(title='Project test')
        self.ticket = Ticket.objects.create(
            title = 'Ticket title',
            description = 'Ticket description',
            project = project,
            creator = self.test_user
        )
        self.factory = RequestFactory()
    def test_comment_create_get_not_autheticated(self):
        request = self.factory.get('tickets:create_comment')
        request.user = AnonymousUser()
        response = CommentCreateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 302)
    def test_comment_create_get_autheticated(self):
        request = self.factory.get('tickets:create_comment')
        request.user = self.test_user
        response = CommentCreateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 200)
    def test_comment_create_post_autheticated(self):
        request = self.factory.post('tickets:create_comment')
        request.user = self.test_user
        response = CommentCreateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 200)

class TestTicketUpdateView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='test@#628password'
        )
        self.test_user.save()
        project = Project.objects.create(title='Project test')
        self.ticket = Ticket.objects.create(
            title = 'Ticket title',
            description = 'Ticket description',
            project = project,
            creator = self.test_user
        )
        self.factory = RequestFactory()
    def test_ticket_update_get_not_autheticated(self):
        request = self.factory.get('tickets:update_ticket')
        request.user = AnonymousUser()
        response = TicketUpdateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 302)
    def test_ticket_update_get_autheticated(self):
        request = self.factory.get('tickets:update_ticket')
        request.user = self.test_user
        response = TicketUpdateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 200)
    def test_ticket_update_post_autheticated(self):
        request = self.factory.post('tickets:update_ticket')
        request.user = self.test_user
        response = TicketUpdateView.as_view()(request, pk=self.ticket.pk)
        self.assertEquals(response.status_code, 200)
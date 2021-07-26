from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from tickets.models import Project, Ticket, TicketComment, TicketAssignment
from .serializers import ProjectSerializer, TicketSerializer, UserSerializer, TicketCommentSerializer, TicketAssignmentSerializer
from rest_framework import viewsets
from rest_framework.views import APIView


class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('title')
    serializer_class = TicketSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('title')
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TicketAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TicketAssignment.objects.order_by('pk')
    serializer_class = TicketAssignmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class TicketCommentViewSet(viewsets.ModelViewSet):
    queryset = TicketComment.objects.order_by('created_on')
    serializer_class = TicketCommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

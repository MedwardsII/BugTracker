from . import views
from django.conf.urls import include
from  django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'comments', views.TicketCommentViewSet)
router.register(r'assignments', views.TicketAssignmentViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('login', views.Login.as_view(), name='login')
]
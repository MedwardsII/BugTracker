'''Tickets URL module'''
from  django.urls import path
from . import views


app_name = 'tickets'
urlpatterns = [
    path('all', views.TicketListView.as_view(), name='list_all'),
    path('assigned', views.TicketAssignedListView.as_view(), name='list_assigned'),
    path('pending', views.TicketNotResolvedListView.as_view(), name='list_pending'),
    path('resolved', views.TicketResolvedListView.as_view(), name='list_resolved'),
    path(
        'pending_assignment',
        views.TicketNeedAssignmentListView.as_view(),
        name='list_need_assignment'
    ),
    path('<int:pk>', views.TicketDetailView.as_view(), name='details'),
    path('update/<int:pk>', views.TicketUpdateView.as_view(), name='update_ticket'),
    path('create/', views.TicketCreateView.as_view(), name='create_ticket'),
    path('create/comment/<int:pk>', views.CommentCreateView.as_view(), name='create_comment'),
    path('entry_success', views.FormSuccessView.as_view(), name='entry_success'),
]

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import F
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Ticket, TicketAssignment
from .forms import TicketCommentForm, TicketAssignmentForm, TicketForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .ticket_helper_functions import populate_viewed_tickets, change_ticket_assignment, \
    post_comment, destroy_assignment

# Create your views here.
@method_decorator(login_required, name='dispatch')
class TicketListView(ListView):
    template_name = 'tickets/ticket_listing.html'
    model = Ticket
    context_object_name = 'tickets'

class TicketNotResolvedListView(TicketListView):
    queryset = Ticket.objects.filter(is_resolved='No')

class TicketResolvedListView(TicketListView):
    queryset = Ticket.objects.filter(is_resolved='Yes')

class TicketNeedAssignmentListView(TicketListView):
    queryset = Ticket.objects.filter(
            is_resolved='No'
        ).exclude(ticketassignment__ticket=F('pk'))

@method_decorator(login_required, name='dispatch')
class TicketAssignedListView(TicketListView):
    def get_queryset(self):
        return Ticket.objects.filter(
            ticketassignment__assigned_user=self.request.user
        )

@method_decorator(login_required, name='dispatch')
class TicketDetailView(DetailView):
    template_name = 'tickets/ticket_details.html'
    queryset = Ticket.objects.all()
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        '''Query of viewed ticket'''
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        ticket = get_object_or_404(Ticket, pk=object.pk)
        populate_viewed_tickets(self.request, ticket)
        ticket_assignment = TicketAssignment.objects.filter(ticket=ticket)
        if ticket_assignment:
            context['assignment'] = ticket_assignment[0]
        return context

@method_decorator(login_required, name='dispatch')
class TicketUpdateView(UpdateView):
    template_name = 'tickets/ticket_edit.html'
    model = Ticket
    context_object_name = 'ticket'
    fields = [
        'request_type',
        'is_resolved',
        'priority'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        ticket = get_object_or_404(Ticket, pk=object.pk)
        context['comment_form'] = TicketCommentForm()
        # get user assigned to ticket
        ticket_assignment = TicketAssignment.objects.filter(ticket=ticket)
        if ticket_assignment:
            context['assignment'] = ticket_assignment[0]
            context['assignment_form'] = TicketAssignmentForm(initial={
                'assigned_user': ticket_assignment[0].assigned_user
            })
        else:
            context['assignment_form'] = TicketAssignmentForm(use_required_attribute=False)
        return context

    def form_valid(self, form):
        object = self.get_object()
        ticket = get_object_or_404(Ticket, pk=object.pk)

        comemnt_form = TicketCommentForm(self.request.POST)
        if comemnt_form.is_valid():
            post_comment(ticket, comemnt_form, self.request.user)

        assignment_form = TicketAssignmentForm(self.request.POST)
        if assignment_form.is_valid():
            change_ticket_assignment(ticket, assignment_form)

        if form.is_valid():
            if form.cleaned_data['is_resolved'] == 'Yes':
                destroy_assignment(ticket)

        return super().form_valid(form)

    def get_success_url(self):
        object = self.get_object()
        return reverse('tickets:details', kwargs={'pk':object.pk})

@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):
    template_name = 'tickets/ticket_create.html'
    form_class = TicketForm
    queryset = Ticket.objects.all()

    def form_valid(self, form):
        form.instance.creator = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tickets:entry_success')

@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    template_name = 'tickets/ticket_comment.html'
    form_class = TicketCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        form.instance.ticket = ticket
        form.instance.creator = self.request.user
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        return reverse('tickets:details', kwargs={'pk':ticket.pk})

class FormSuccessView(View):
    template_name = 'tickets/ticket_created_success.html'

    def get(self, request):
        data = {
            'success_message': 'Entry submitted successful!',
            'page_name': 'Ticket Submission'
        }
        return render(request, self.template_name, data)

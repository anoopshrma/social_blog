from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(generic.DetailView):
    model=Group

class ListGroup(generic.ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug')) #Accessing the Group
        try:
            GroupMember.objects.create(user=self.request.user,group=group)# If the user is not registered in the group then the current user joins the Group as new groupmember.

        except IntegrityError:
            messages.warning(self.request,'You alrady a member') #if the current user is already a member then this 

        else:
            messages.warning(self.request,'You joined the Group') #if its a new user then this 

        return super().get(request,*args,**kwargs) #overrides the get method and saves the new info in GroupMember if a new user is added.


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        try:
            membership=GroupMember.objects.filter(
            user=self.request.user,
            group__slug=self.kwargs.get('slug')
          ).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request,'You are not a member')

        else:
            membership.delete()
            messages.success(self.request,'You left the group')

        return super().get(request,*args,**kwargs)


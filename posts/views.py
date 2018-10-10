from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin 
# Create your views here.
from posts.models import Post
from posts import forms
from django.contrib.auth import get_user_model
User=get_user_model()

class PostList(SelectRelatedMixin,generic.ListView):
    model=Post
    select_related=('user','group') #Connects foreignkey elements 


class UserPostList(generic.ListView):
    model=Post
    template_name='posts/user_post_list.html'
    
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['post_user']=self.post_user #Returns all the user posts fetched through the query        
        return context



class PostDetail(SelectRelatedMixin,generic.DetailView):
    model=Post
    select_related=('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields=('message','group')
    model=Post
#This method checks whether the form is valid or invalid
#if valid then it connects the post to the user 
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user #yahan pr connect ho ra h 
        self.object.save()
        return super().form_valid(form)

class DeletePost(generic.DeleteView,LoginRequiredMixin,SelectRelatedMixin):
    model=Post
    select_related=('user','group')
    success_url=reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'post deleted')
        return super().delete(*args,**kwargs)
        



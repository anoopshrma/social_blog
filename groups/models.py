from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
import misaka #it renders template tag for markdown 

from django.contrib.auth import get_user_model #To get the model details of the active User
User=get_user_model() #Now User variable has access to all the model details.

from django import template #this  
register=template.Library()

class Group(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='')
    description_html=models.TextField(editable=False,default='',blank=True)
    members=models.ManyToManyField(User,through='GroupMember') #It'll show all the group member of a group. if they join the group.
    
    def __str__(self):
        return self.name

#This save method overrides the default data stored in database with these data.
#misaka.html is rendering markdown for converting the textfield data into html based text.
    def save(self,*args,**kwargs): 
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})
        
        
    class Meta:
            ordering=['name']


class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_group',on_delete=models.CASCADE) #here we have given user a related_name of user group which is being accessed as 'get' bcoz of the upper imported library template. BAsically it allowed us to link post to group member.

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=('group','user')

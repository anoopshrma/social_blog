from django.contrib import admin
from .models import Group,GroupMember
# Register your models here.

#Inline method will store the follwing model inside the registering model.
#for eg: we'll see GroupMember as Group=>GroupMember
class GroupMemberInline(admin.TabularInline):
    model=GroupMember
admin.site.register(Group)
from django.db import models
from django.contrib import auth
# Create your models here.

#This class creates a user model for the user 
#Django does all the work back-end to create this.
#Authorisation is checked by auth module.
class User(auth.models.User,auth.models.PermissionsMixin):
    

    def __str__(self):
        return '@{}'.format(self.username)


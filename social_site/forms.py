from django.contrib.auth import get_user_model #It'll fetch the current user model
from django.contrib.auth.forms import UserCreationForm #Django already has a UsercreationForm present which enables to create a  user signup page without much effort

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields=('username','email','password1','password2')
        model=get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(self, *args, **kwargs) #This method is overriding the content before showing it.
            self.fields['username'].label='Display Name' # This is customising the name 'username' so that it is easily undestood by the user
            self.fields['email'].label='Email Address'
               
            
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
class newTask(forms.ModelForm):
    class Meta:
        model = models.Tasks
        exclude = ('user','completeStatus')
    
class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
    class Meta:
        model = models.User
        fields = ['fullName','username','profilePhoto','profession','password1']
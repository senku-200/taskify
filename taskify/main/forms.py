from django import forms
from . import models
class newTask(forms.ModelForm):
    class Meta:
        model = models.Tasks
        exclude = ('user','completeStatus')
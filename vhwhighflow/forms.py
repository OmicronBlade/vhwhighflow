from django import forms
from .models import highflow, sats

class DateInput(forms.DateInput):
    input_type = 'date'

class highflowForm(forms.ModelForm):
    highflow = forms.FileField()

    #class Meta:
    #    model = vhwhighflow
    #    fields = ['Name','FolderNo','Date']
    #    widgets = {
    #        'Date': forms.DateTimeInput,
    #    }

class satsForm(forms.ModelForm):
    #sats = forms.FileField()

    class Meta:
        model = sats
        fields = ('Date', 'Sats',)

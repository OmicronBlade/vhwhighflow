from django import forms
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from .models import highflow, sats

class DateInput(forms.DateInput):
    input_type = 'date'

class highflowFormCreate(forms.ModelForm):
    #highflow = forms.FileField()
    class Meta:
        model = highflow
        fields = ['FolderNo','Name','Age','Background','PriorityScore',
                  'PriorityScoreDate','HFStart']
        widgets = {
            'PriorityScoreDate': DatePickerInput(),
            'HFStart': DatePickerInput(),
        }

class highflowFormUpdate(forms.ModelForm):
    #highflow = forms.FileField()
    class Meta:
        model = highflow
        fields = ['FolderNo', 'Name', 'Age', 'Background', 'PriorityScore',
                  'PriorityScoreDate', 'UpdatedPriority', 'UpdatedPriorityDate', 'HFStart', 'Archive']
        widgets = {
            'PriorityScoreDate': DatePickerInput(format='%d/%m/%Y'),
            'UpdatedPriorityDate': DatePickerInput(format='%d/%m/%Y'),
            'HFStart': DatePickerInput(format='%d/%m/%Y'),
        }

class satsForm(forms.ModelForm):
    #sats = forms.FileField()

    class Meta:
        model = sats
        fields = ['Date', 'RespRate','HeartRate','Sats','FiO2','Litres']
        widgets = {
            'Date': DateTimePickerInput(format='%d/%m/%Y'),
        }

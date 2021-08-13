from django import forms
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from .models import highflow, sats

class DateInput(forms.DateInput):
    input_type = 'date'

class highflowFormCreate(forms.ModelForm):
    #highflow = forms.FileField()
    class Meta:
        model = highflow
        fields = ['FolderNo','Name','Age','Ward','AdmissionDate','Background','PriorityScore',
                  'PriorityScoreDate','HFStart']
        widgets = {
            'AdmissionDate': DatePickerInput(format='%d/%m/%Y'),
            'PriorityScoreDate': DatePickerInput(format='%d/%m/%Y'),
            'HFStart': DatePickerInput(format='%d/%m/%Y'),
            'Background': forms.Textarea(attrs={'rows': 5, 'cols': 25})
        }

class highflowFormUpdate(forms.ModelForm):
    #highflow = forms.FileField()
    class Meta:
        model = highflow
        fields = ['FolderNo', 'Name', 'Age', 'Ward', 'Background', 'PriorityScore', 'AdmissionDate',
                  'PriorityScoreDate', 'UpdatedPriority', 'UpdatedPriorityDate', 'HFStart', 'Archive']
        widgets = {
            'AdmissionDate': DatePickerInput(format='%d/%m/%Y'),
            'PriorityScoreDate': DatePickerInput(format='%d/%m/%Y'),
            'UpdatedPriorityDate': DatePickerInput(format='%d/%m/%Y'),
            'HFStart': DatePickerInput(format='%d/%m/%Y'),
            'Background': forms.Textarea(attrs={'rows': 5, 'cols': 25})
        }

class satsForm(forms.ModelForm):
    #sats = forms.FileField()

    class Meta:
        model = sats
        fields = ['Date', 'RespRate','HeartRate','Sats','FiO2','Litres']
        widgets = {
            'Date': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
        }

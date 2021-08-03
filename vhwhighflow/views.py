from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import *
from .forms import highflowForm, satsForm

class highflowCreate(CreateView):
    model = highflow
    fields = ['FolderNo','Name','Age','RedScore']
    #form_class = highflowForm
    success_url = '/'

class highflowInidividual(DetailView):
    model = highflow

class highflowList (ListView):
    model = highflow
    fields = ['Name','Age','RedScore']
    queryset = highflow.objects.filter(Archive=False)

class highflowUpdateView(UpdateView):
    model = highflow
    fields = ['FolderNo','Name','Age','RedScore','Archive']

    def get_success_url(self):
        return reverse('list', kwargs={'pk': self.object.pk})

class satsCreate(CreateView):
    model = sats
    form_class = satsForm

    def form_valid(self, form):
        form.instance.Patient_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list', kwargs={'pk': self.object.Patient_id})

class satsUpdateView(UpdateView):
    model = sats
    fields = ['Date','Sats']
    success_url = '/'



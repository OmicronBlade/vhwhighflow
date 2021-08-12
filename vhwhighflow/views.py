from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.urls import reverse
from .models import *
from .forms import highflowFormCreate, highflowFormUpdate, satsForm

class highflowDashboard(ListView):
    model = highflow
    template_name = 'vhwhighflow/highflow_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = highflow.objects.filter(Archive=False)
        context['on_highflow'] = queryset.filter(~Q(HFStart=None)).count()
        context['reds'] = queryset.filter(HFStart=None).count()
        return context


    #queryset = highflow.objects.filter(Archive=False).filter(~Q(HFStart=None))
    #print(highflow.objects.filter(Archive=False).filter(~Q(HFStart=None)))

class highflowCreate(CreateView):
    model = highflow
    #fields = ['FolderNo','Name','Age','Background','PriorityScore',
    #          'PriorityScoreDate','HFStart']
    form_class = highflowFormCreate
    success_url = 'list'

class highflowInidividual(DetailView):
    model = highflow

class highflowList (ListView):
    model = highflow
    fields = ['Name','Age','PriorityScore','UpdatedPriority','HFStart']
    queryset = highflow.objects.filter(Archive=False).filter(~Q(HFStart=None))
    ordering = ['HFStart']

class highflowRedList (ListView):
    model = highflow
    template_name = 'vhwhighflow/red_list.html'
    fields = ['Name','Age','PriorityScore','UpdatedPriority','AdmissionDate']
    queryset = highflow.objects.filter(HFStart=None)
    ordering = ['AdmissionDate']

class highflowListAll (ListView):
    model = highflow
    fields = ['Name','Age','PriorityScore','UpdatedPriority','HFStart']
    ordering = ['HFStart']

class highflowUpdateView(UpdateView):
    model = highflow
    #fields = ['FolderNo','Name','Age','Background','PriorityScore',
    #          'PriorityScoreDate','UpdatedPriority','UpdatedPriorityDate','HFStart','Archive']
    form_class = highflowFormUpdate

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
    #fields = ['Date', 'RespRate','HeartRate','Sats','FiO2','Litres']
    form_class = satsForm

    def get_success_url(self):
        return reverse('list', kwargs={'pk': self.object.Patient_id})

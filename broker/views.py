from .models import Broker
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import BrokerForm

class BrokerListView(ListView):
    model = Broker
    template_name = 'broker/list.html'
    context_object_name = 'brokers'

class BrokerCreateView(CreateView):
    model = Broker
    template_name = 'broker/form.html'
    form_class = BrokerForm
    success_url = '/brokers/'

class BrokerUpdateView(UpdateView):
    model = Broker
    template_name = 'broker/form.html'
    form_class = BrokerForm
    success_url = '/brokers/'


class BrokerDetailView(DetailView):
    model = Broker
    template_name = 'broker/detail.html'


class BrokerDeleteView(DeleteView):
    model = Broker
    template_name = 'broker/confirm_delete.html'
    success_url = '/brokers/'
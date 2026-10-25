from .models import Feature
from django.views.generic import CreateView, ListView, UpdateView
from .forms import FeatureForm


class FeatureListView(ListView):
    model = Feature
    template_name = 'features/list.html'
    context_object_name = 'features'

class FeatureCreateView(CreateView):
    model = Feature
    template_name = 'features/form.html'
    form_class = FeatureForm
    success_url = '/features/'


class FeatureUpdateView(UpdateView):
    model = Feature
    template_name = 'features/form.html'
    form_class = FeatureForm
    success_url = '/features/'



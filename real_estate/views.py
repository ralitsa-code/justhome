from .models import RealEstate
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class RealEstateListView(ListView):
    model = RealEstate
    template_name = 'real_estate/list.html'
    context_object_name = 'real_estates'


class RealEstateCreateView(CreateView):
    model = RealEstate
    template_name = 'real_estate/form.html'
    fields = [
        'real_estate_type',
        'address',
        'area',
        'price',
        'description',
        'main_image',
        'broker',
        'feature',
    ]
    success_url = '/properties/'


class RealEstateDetailView(DetailView):
    model = RealEstate
    template_name = 'real_estate/detail.html'


class RealEstateUpdateView(UpdateView):
    model = RealEstate
    template_name = 'real_estate/form.html'
    fields = [
        'real_estate_type',
        'address',
        'area',
        'price',
        'description',
        'main_image',
        'broker',
        'feature',
    ]
    success_url = '/properties/'


class RealEstateDeleteView(DeleteView):
    model = RealEstate
    template_name = 'real_estate/confirm_delete.html'
    success_url = '/properties/'
    context_object_name = 'real_estate'




from multiprocessing import context

from .models import RealEstate
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import RealEstateForm

class RealEstateListView(ListView):
    model = RealEstate
    template_name = 'real_estate/list.html'
    context_object_name = 'real_estates'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(address__icontains=query)

        property_type = self.request.GET.get('type')

        if property_type:
            queryset = queryset.filter(real_estate_type=property_type)


        sort_order = self.request.GET.get('sort')

        if sort_order == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_order == 'price_desc':
            queryset = queryset.order_by('-price')

        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_properties'] = RealEstate.objects.exists()
        return context


class RealEstateCreateView(CreateView):
    model = RealEstate
    template_name = 'real_estate/form.html'
    form_class = RealEstateForm
    success_url = '/properties/'


class RealEstateDetailView(DetailView):
    model = RealEstate
    template_name = 'real_estate/detail.html'


class RealEstateUpdateView(UpdateView):
    model = RealEstate
    template_name = 'real_estate/form.html'
    form_class = RealEstateForm
    success_url = '/properties/'


class RealEstateDeleteView(DeleteView):
    model = RealEstate
    template_name = 'real_estate/confirm_delete.html'
    success_url = '/properties/'
    context_object_name = 'real_estate'




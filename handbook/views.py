from django.views.generic import DetailView, ListView

from fields.models import Crop
from handbook.models import Fertilizer , Pest


# class CategoryView(ListView):
#     model = Category
#     template_name = 'handbook/category_list.html'
#     context_object_name = 'categories'
#
#     def get_queryset(self):
#         return Category.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(CategoryView, self).get_context_data(**kwargs)
#         context['fertilizers'] = Fertilizer.objects.all()
#
#         return context


class FertilizerView(ListView):
    model = Fertilizer
    template_name = 'handbook/fertilizer_list.html'
    context_object_name = 'fertilizers'


class FertilizerDetail(DetailView):
    model = Fertilizer
    template_name = 'handbook/fertilizer_detail.html'
    context_object_name = 'fertilizer'


class PestView(ListView):
    model = Pest
    template_name = 'handbook/pest_list.html'
    context_object_name = 'pests'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')

        if search_query:
            return Pest.objects.filter(name__icontains=search_query)
        else:
            return Pest.objects.all()


class PestDetail(DetailView):
    model = Pest
    template_name = 'handbook/pest_detail.html'
    context_object_name = 'pest'

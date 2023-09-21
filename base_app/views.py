from django.views.generic import ListView, DetailView
from django.db.models import Q


from .models import *
from .forms import SearchForm


class HomeView(ListView):
    model = Vacancy
    form_class = SearchForm
    paginate_by = 5
    template_name = 'base_app/home.html'
    extra_context = {'title': 'Home', 'method': 'get',
                     'submit': 'search'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.queries)
        return context

    def get_queryset(self, *args, **kwargs):
        fields = self.form_class.declared_fields.keys()
        self.queries = {k: v for k, v in self.request.GET.items()
                        if v and k in fields}
        sch = self.queries.pop('search', '')
        queryset = self.model.objects.filter(
            Q(title__icontains=sch), **self.queries)
        self.queries['search'] = sch
        return queryset


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'base_app/vacancy.html'

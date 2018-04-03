from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Login_Registration.Model import SiddhuModel

class SiddhuList(ListView):
    model = SiddhuModel

class SiddhuInsert(CreateView):
    model = SiddhuModel
    success_url = reverse_lazy('siddhu_list')
    fields = ['name', 'address', 'emailid']

class SiddhuUpdate(UpdateView):
    model = SiddhuModel
    success_url = reverse_lazy('siddhu_list')
    fields = ['name', 'address', 'emailid']

class SiddhuDelete(DeleteView):
    model = SiddhuModel
    success_url = reverse_lazy('siddhu_list')
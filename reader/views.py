from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory

from .models import Reader
from .forms import ReaderForm


def reader_list(request):
    template = loader.get_template('reader_list.html')
    reader = Reader.objects.all()
    reader_data = {
        "objects_list": reader,
    }
    return HttpResponse(template.render(reader_data, request))


class ReaderCreate(CreateView):
    model = Reader
    form_class = ReaderForm
    template_name = 'reader_create.html'
    success_url = reverse_lazy('reader:reader_list')


class ReaderEdit(UpdateView):  
    model = Reader  
    form_class = ReaderForm  
    template_name = 'reader_edit.html'  
    success_url = reverse_lazy('reader:reader_list')  


class ReaderDelete(DeleteView):
    model = Reader
    success_url = reverse_lazy('reader:reader_list')

from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views.generic import CreateView
from .models import BagReport
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def index (request):
    return render(request, 'SendReport/bagreport_form.html')
def success (request):
    return render(request, 'SendReport/success.html')

class BagReportCreateView (SuccessMessageMixin,CreateView):
    model = BagReport
    fields = ('name_user','text','phone')
    template_name = 'SendReport/bagreport_form.html'
    success_url = reverse_lazy('great')
    success_message = "Новая заявка успешно добавлена!!!"

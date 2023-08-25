from django.shortcuts import render, redirect,HttpResponseRedirect, reverse
from django.views.generic import CreateView
from .models import BagReport
from django.contrib import messages
from django.urls import reverse_lazy
from .models import BagReport
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
def index (request):
    return render(request, 'SendReport/base.html')
def success (request):
    reports = BagReport.objects.all()[::-1]
    return render(request, 'SendReport/success.html',{'reports':reports})

class BagReportCreateView (SuccessMessageMixin,CreateView):
    model = BagReport
    fields = ('name_user','text','phone')
    success_message = ' was created successfully'
    def get_success_url(self):
        return reverse('great')



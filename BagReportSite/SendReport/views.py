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
    reports = BagReport.objects.latest('id')
    return render(request, 'SendReport/success.html',{'reports':reports})

def search (request):

    search_query = request.GET.get('search','')
    if search_query:
        reports = BagReport.objects.filter(id=search_query)
    else:

        reports = BagReport.objects.all()
    return render(request, 'SendReport/search.html',{'reports':reports})

class BagReportCreateView (SuccessMessageMixin,CreateView):
    model = BagReport
    fields = ('name_user','text','phone')
    success_message = ' was created successfully'
    def get_success_url(self):
        return reverse('great')



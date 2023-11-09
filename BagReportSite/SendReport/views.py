from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .models import BagReport
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'SendReport/base.html')


def success(request):
    reports = BagReport.objects.latest('id')
    return render(request, 'SendReport/success.html', {'reports': reports})


def search(request):
    search_query = request.GET.get('search', '')
    try:
        search_query = int(search_query)
    except ValueError:
        search_query = None
    reports = BagReport.objects.filter(id=search_query)
    return render(request, 'SendReport/search.html', {'reports': reports})
#aboba

class BagReportCreateView(SuccessMessageMixin, CreateView):
    model = BagReport
    fields = ('name_user', 'text', 'phone')
    success_message = ' was created successfully'

    def get_success_url(self):
        return reverse('great')



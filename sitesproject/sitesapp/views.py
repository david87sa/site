from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views import View


from .models import Site
from .models import Section
from .models import Guest
from .forms import ConFirmForm
import logging

logger = logging.getLogger(__name__)
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sitesapp/index.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all()

class SiteDetail(View):
    template_name = 'sitesapp/site_detail.html'
    context_object_name = 'sections'
    form_class = ConFirmForm

    def get(self, request,*args,**kwargs):

        self.guest = Guest.objects.get(id=kwargs.get('guestid'))
        self.sitetheme = Site.objects.get(name=kwargs.get('site')).theme

        return render(request,self.template_name,{'sections':Section.objects.all(),'guest':self.guest,'sitetheme':self.sitetheme})    

    def post(self, request, *args, **kwargs):
        
        data =request.POST

        self.guest = Guest.objects.get(id=data.get('id'))

        self.guest.confirmed=data.get('confirmed')
        self.guest.save()

        return render(request, 'sitesapp/response.html', {'response': self.guest.confirmed})


class ContactFormView(FormView):
    template_name = 'sitesapp/response.html'
    form_class = ConFirmForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        
        return super().form_valid(form)        
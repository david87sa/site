from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Miembro

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'miembros'

    def get_queryset(self):
        return Miembro.objects.order_by('-nombre')[:5]

class DetailView(generic.DetailView):
    model = Miembro
    template_name = 'polls/detail.html'
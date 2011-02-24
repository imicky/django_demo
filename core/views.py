from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from django_demo.core.models import Entry

def index(request):
    return render_to_response('core/index.html', context_instance=RequestContext(request))

def list(request):
    entry_list = Entry.objects.all()
    return render_to_response('core/list.html', {'entry_list': entry_list})

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from nymdesign.portfolio.models import *

def view_contact(request):
    """
    View Contact Page
    """
    
    lu = { 
        'title' : 'Contact'
        ,'media_types' : MediaType.objects.all().order_by('sort_order')        
    }

    return render_to_response('info_pages/contact.html', lu, context_instance=RequestContext(request))
    
def view_about(request):
    """
    View About Page
    """

    lu = { 
        'title' : 'About'
        ,'media_types' : MediaType.objects.all().order_by('sort_order')        
    }

    return render_to_response('info_pages/about.html', lu, context_instance=RequestContext(request))

def view_clients(request):
    """
    View Cients Page
    """

    lu = { 
        'title' : 'Clients'
        ,'clients' : Client.objects.all()        
        ,'media_types' : MediaType.objects.all().order_by('sort_order')        
    }

    return render_to_response('info_pages/clients.html', lu, context_instance=RequestContext(request))



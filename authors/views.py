from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def profile(request):

	return render_to_response('profile.html',
                          {},
                          context_instance=RequestContext(request))

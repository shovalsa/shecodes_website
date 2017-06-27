from django.shortcuts import render, get_object_or_404
from .models import User, Branch, Track
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, "index.html", {'users': users})

@login_required #only logged in users can enter this page.
def members(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "members.html", {'user': user})

def tracks(request):
    tracks = Track.objects.all()
    return render(request, "tracks.html", {'track': tracks})


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response




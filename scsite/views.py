from django.shortcuts import render, get_object_or_404
from .models import User, Branch, Track, Team
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, "index.html")

@login_required #only logged in users can enter this page.
def members(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "members.html", {'user': user})

def members_index(request):
    users = User.objects.all()
    return render(request, "members_index.html", {'users': users})

def tracks(request):
    tracks = Track.objects.all()
    return render(request, "tracks.html", {'tracks': tracks})

def team(request):
    team = Team.objects.all()
    return render(request, "team.html", {'team': team})

def branches(request):
    branches = Branch.objects.all()
    return render(request, "branches.html", {'branches': branches})

def next_generation(request):
    return render(request, "next_generation.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")

def partners(request):
    return render(request, "partners.html")

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response




from django.shortcuts import render, get_object_or_404
from .models import User, Branch, Track, Team, Faq, News, Job, Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
# Create your views here.

def index(request):
    jobs = Job.objects.all()
    news = News.objects.all()
    event_list = Event.objects.all()
    events= []
    for event in event_list:
        if event.is_upcoming() == True:
            events.append(event)
    return render(request, "index.html", {'news': news, 'jobs':jobs, 'events': events})

@login_required #only logged in users can enter this page.
def members(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "members.html", {'user': user})

def members_index(request):
    users = User.objects.all()
    return render(request, "members_index.html", {'users': users})

# @login_required #only logged in users can enter this page.
def jobs(request):
    jobs = Job.objects.all()
    return render(request, "jobs.html", {'jobs': jobs})

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
    branches = Branch.objects.all()
    return render(request, "next_generation.html", {'branches': branches})

def faq(request):
    faq = Faq.objects.all()
    return render(request, "faq.html", {'faq': faq})

def contact(request):
    return render(request, "contact.html")

def partners(request):
    return render(request, "partners.html")

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def about(request):
    return render(request, "about.html")


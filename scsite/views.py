from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Branch, Track, Team, Faq, News, Job, Event, User, Profile
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import timezone
from .forms import SignUpForm, ContactForm, UserCreationForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.utils import formats


@login_required()
def home(request):
    return render(request, 'index.html')

@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            login(request, user)
            return redirect('home')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})


def contact(request):
    if request.method == 'GET':
        contact = ContactForm()
    else:
        contact = ContactForm(request.POST)
        if contact.is_valid():
            subject = contact.cleaned_data.get('subject')
            from_email = contact.cleaned_data.get('contact_email')
            message = contact.cleaned_data.get('message')
            name = contact.cleaned_data.get('contact_name')
            everything = "Name: %s\n\nSubject: %s\n\nEmail: %s \n\nMessage: %s \n\n"%(str(name), str(subject), str(from_email), str(message))
            try:
                send_mail(subject, everything, from_email, ['contact.shecodes@gmail.com'])
            except BadHeaderError:
                return HttpResponse(_('Invalid header found.'))
            return success(request)
    return render(request, "contact.html", {'contact': contact})

def success(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, "success.html")

def index(request):
    jobs = Job.objects.all()
    news = News.objects.all()
    event_list = Event.objects.all()
    events= []
    for event in event_list:
        if event.is_upcoming() == True:
            events.append(event)
            formatted_datetime = formats.date_format(event.event_date, "SHORT_DATETIME_FORMAT")
            event.event_date = str(formatted_datetime)
    return render(request, "index.html", {'news': news, 'jobs':jobs, 'events': events})


@login_required #only logged in users can enter this page.
def members(request, id):
    user = get_object_or_404(User, id=id)
    profile = Profile.objects.all()
    return render(request, "members.html", {'user': user, 'profile': profile})

def members_index(request):
    users = User.objects.all()
    return render(request, "members_index.html", {'users': users})

# @login_required #only logged in users can enter this page.
def jobs(request):
    jobs = Job.objects.all()
    return render(request, "jobs.html", {'jobs': jobs})

def newsletter(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "newsletter.html", {'news': news})

def newsletter_index(request):
    news = News.objects.all()
    return render(request, "newsletter_index.html", {'news': news})



def tracks(request):
    tracks = Track.objects.all()
    return render(request, "tracks.html", {'tracks': tracks})

def team(request):
    team = Team.objects.all()
    return render(request, "team.html", {'team': team})

def branches(request):
    branches = Branch.objects.all()
    proj = Track.objects.all()[1]
    project_branches = []
    for branch in branches:
            if proj in branch.availableTracks.all():
                project_branches.append(branch)
    return render(request, "branches.html", {'branches': branches, 'project_branches': project_branches})

def next_generation(request):
    branches = Branch.objects.all()
    return render(request, "next_generation.html", {'branches': branches})

def faq(request):
    faq = Faq.objects.all()
    return render(request, "faq.html", {'faq': faq})

def partners(request):
    return render(request, "partners.html")

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def about(request):
    return render(request, "about.html")


from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Profile, Branch, Track, Team, Faq, News, Job, Event, User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import timezone
from .forms import SignUpForm, ContactForm
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


@login_required()
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.join_date = form.cleaned_data.get('join_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def contact(request):
    if request.method == 'GET':
        contact = ContactForm()
    else:
        contact = ContactForm(request.POST)
        if contact.is_valid():
            subject = contact.cleaned_data.get('subject')
            from_email = contact.cleaned_data.get('from_email')
            message = contact.cleaned_data.get('message')
            try:
                send_mail(subject, message, from_email, ['shovatz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return success(request)
    return render(request, "contact.html", {'contact': contact})

def success(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, "success.html")

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

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
    profile = get_object_or_404(Profile, id=id)
    return render(request, "members.html", {'user': user, 'profile': profile})

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

def partners(request):
    return render(request, "partners.html")

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def about(request):
    return render(request, "about.html")


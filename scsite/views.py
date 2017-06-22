from django.shortcuts import render, get_object_or_404
from .models import User, Branch, Track
# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, "index.html", {'users': users})

def detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "detail.html", {'user': user})


# def branches(request, id):
#     branch = get_object_or_404(Branch, id=id)
#     return render(request, "detail.html", {'branch': branch})


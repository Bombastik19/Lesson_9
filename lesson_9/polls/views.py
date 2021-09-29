from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
class CigaretteListView(ListView):

    model = Cigarette
    queryset = Cigarette.objects.filter(status = True)
    template_name = 'home.html'

class CigaretteDetailView(DetailView):
    model = Cigarette
    template_name = 'home_detail.html'
    context_object_name = 'Cigarette'

def account(request):
    if request.user.is_authenticated:
        users = request.user
        return render(request,'account/profile.html',{'user':users})   
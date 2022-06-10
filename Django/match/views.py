from multiprocessing import context
from django.shortcuts import render
from .models import Match
# Create your views here.

def display_match(request):
  matches= Match.objects.filter(home_goals__gte=5)
  context={
    'matches':matches
  }

  return render(request,'match/match_list.html',context)

def all_matches(request):
  all_matches= Match.objects.all()
  context={
    'all_matches':all_matches
  }
  return render(request,'match/all_matches.html',context)

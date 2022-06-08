from django.shortcuts import render
from club.models import Club

def club_list(request):
  context = Club.objects.all()

  return render(request,'club/club_list.html',context)
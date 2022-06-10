from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from club.models import Club

def club_list(request):
  clubs = Club.objects.all()
  context ={'clubs':clubs}

  return render(request,'club/club_list.html',context)


def club_detail(request,pk):
  # club=Club.objects.get(id=pk)

  context = {'club':get_object_or_404(Club,id=pk)}

  return render(request,'club/club_detail.html',context)
  
def club_order(request):
  clubs=Club.objects.order_by('year')
  context = {'clubs':clubs}

  return render(request,'club/club_ordered.html',context)
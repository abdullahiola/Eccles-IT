from django.conf.urls import patterns,url
from club.views import club_list

urlpatterns = patterns('',
  url(
    regex=r"^$",
    view=club_list,
    name='club_list'  
  ),
    
)

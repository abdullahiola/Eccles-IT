from django.contrib import admin
from .models import Match


class MatchAdmin(admin.ModelAdmin):
  list_per_page = 20
  list_filter= ['home_goals','away_goals']
  search_field = ['home_club__name','away_club__name']
  date_hierarchy = 'date'
  # list_display= ['name','year','ground']

admin.site.register(Match,MatchAdmin)

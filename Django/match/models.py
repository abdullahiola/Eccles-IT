from django.db import models
from club.models import Club

class Match(models.Model):
  """Model of a football match."""

  date = models.DateField()
  home_club = models.ForeignKey(Club, related_name="home_matches",on_delete=models.CASCADE)
  away_club = models.ForeignKey(Club, related_name="away_matches",on_delete=models.CASCADE)
  home_goals = models.IntegerField()
  away_goals = models.IntegerField()

  class Meta:
    get_latest_by = "date"
    ordering = ["date"]
    verbose_name_plural = "matches"

   

  def __str__(self):

    return "{}: {} {:d}-{:d} {}".format(self.date, self.home_club,
      self.home_goals, self.away_goals, self.away_club)

  def is_home_win(self):
    return self.home_goals > self.away_goals

  def is_away_win(self):
    return self.away_goals > self.home_goals

  def is_draw(self):
    return self.home_goals == self.away_goals

  def home_points(self):
    if self.is_home_win():
      return 3
    elif self.is_draw():
      return 1
    else:
      return 0

  def away_points(self):
    if self.is_away_win():
      return 3
    elif self.is_draw():
      return 1
    else:
      return 0  

# Match.objects.filter(home_club__name='Swansea').count()
#Match.objects.filter(home_club__name='Swansea').exclude(home_goals__lte='2').count()
#Match.objects.filter(home_club__year__gte=1900).count() 
# Match.objects.filter(home_club__year__gte=1900).filter(date__startswith=2013).coun
# t()
#stoke.home_matches.filter(home_goals=0).exclude(away_goals__gte=1).count()
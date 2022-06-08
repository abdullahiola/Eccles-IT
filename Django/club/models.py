from django.db import models

# Create your models here.
class Club(models.Model):
  name=models.CharField(max_length=30)
  year=models.PositiveSmallIntegerField("Year established")
  ground= models.CharField(max_length=40)
  capacity= models.PositiveIntegerField(null=True,blank=True)
  website= models.URLField(max_length=50,blank=True)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ['name']

#Club.objects.filter(name__startswith="M")
#Club.objects.filter(name__contains="ham")
#Club.objects.filter(year__gte=1900)
#Club.objects.exclude(ground__contains='stadium').count()
#Club.objects.exclude(name__startswith='S').filter(year__gte=1880).count()
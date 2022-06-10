from . import views

from django.contrib import admin
from django.urls import path,include
urlpatterns = [
  path('',views.club_list,name='club_list'),
  path('club/<str:pk>',views.club_detail,name="club_detail"),
  path('cluborder',views.club_order,name='order')
]

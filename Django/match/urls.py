from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_matches,name='all_matches'),
    path('somematches',views.display_match,name='display_match')
]

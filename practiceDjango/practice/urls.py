from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/practice
    path('',views.all_practice, name='all_practice'),
]


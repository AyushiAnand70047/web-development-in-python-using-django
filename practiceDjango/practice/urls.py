from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/practice
    path('',views.all_practice, name='all_practice'),
    path('chai/<int:chai_id>',views.chai_detail, name='chai_detail'),
    path('chai_store/',views.chai_store_view,name='chai_stores'),
]
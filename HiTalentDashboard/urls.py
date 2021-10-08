from django.urls import path
from HiTalentDashboard import views

app_name = 'app'

urlpatterns = [
    path('dashboard/', views.list_of_candidates, name='dashboard')
]
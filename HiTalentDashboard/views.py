from django.shortcuts import render
from .models import candidate

# Create your views here.

def list_of_candidates(request):
    all_candidates = candidate.objects.all()
    # number_of_candidates = len(all_candidates)
    
    placed_candidates = candidate.objects.filter(candidate_placed=True)
    available_candidates = candidate.objects.filter(candidate_placed=False)

    # number_of_placed_candidates = len(placed_candidates)
    # number_of_available_candidates = len(available_candidates)

    context = {'all_candidates':all_candidates, 'available_candidates':available_candidates, 'placed_candidates':placed_candidates}
    return render(request, 'HiTalentDashboard/dashboard.html', context)
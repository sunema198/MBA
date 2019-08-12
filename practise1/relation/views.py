from django.shortcuts import render
from .models import Relation

def home(request):
	relation = Relation.objects
	return render(request, 'relation/home.html', {'relation':relation}) 

# Create your views here.

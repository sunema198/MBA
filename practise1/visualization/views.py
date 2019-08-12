from django.shortcuts import render
from .models import Visualization

def home(request):
	visualization = Visualization.objects
	return render(request, 'visualization/home.html', {'visualization':visualization}) 

# Create your views here.

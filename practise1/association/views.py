from django.shortcuts import render
from .models import Association

def home(request):
	association = Association.objects
	return render(request, 'association/home.html', {'association':association}) 

# Create your views here.

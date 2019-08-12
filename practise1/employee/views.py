from django.shortcuts import render

from .models import Employee

def home(request):
		employee = Employee.objects
		return render(request, 'employee/home.html', {'employee':employee})

# Create your views here.

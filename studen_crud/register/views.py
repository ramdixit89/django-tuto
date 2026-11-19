from django.shortcuts import render
from django.contrib import messages
from .models import User
from .forms import RegisterForm
# Create your views here.
def register_user(request):
    if request.method == "POST":
      form = RegisterForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request, "Student Registered Sucessfully!")
      else:
         messages.error(request, "Field reuired!" )
    else:
       form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'Register New Student'})
from django.shortcuts import render, get_object_or_404, redirect
from register.models import User
from register.forms import RegisterForm
def main_page(request):
    return render(request, 'homePage.html')

def login_page(request):
    return render(request, 'login.html')

def student_home(request):
    theme = request.GET.get('theme', 'dark')
    if theme == 'dark':
        template_name = 'dark.html'
        current_css_theme = 'css/dark.css'
    else:
        template_name = 'light.html'
        current_css_theme = 'css/light.css'

    return render(request, template_name, {'current_css': current_css_theme})

# 1. Fetch and list all students from the database
def student_list(request):
    # Django ORM: User.objects.all() executes "SELECT * FROM register_user;"
    students = User.objects.all()
    return render(request, 'studentlist.html', {'userData': students})

# 2. Fetch single student detail by primary key (id)
def student_detail(request, studentid):
    # get_object_or_404 safely handles invalid student IDs with a 404 page
    student = get_object_or_404(User, id=studentid)
    return render(request, 'studentdetail.html', {'student': student})

def delete_student(request, studentid):                        
    student = get_object_or_404(User, id=studentid)
    student.delete()
    return redirect('student_list')

def edit_student(request,studentid):
    student = get_object_or_404(User, id=studentid) 

    if request.method == "POST":
      form = RegisterForm(request.POST, instance=student)

      if form.is_valid():
          form.save()
          return redirect('student_list')

    else:
        form = RegisterForm(instance=student)

    return render(request, 'edit_stduent.html', { 'form': form, 'student': student })


from django.shortcuts import render


users = [
    {'id' : 1, 'name': 'jethalal', 'email': 'jethalal@example.com'},
    {'id' : 2, 'name': 'daya', 'email': 'daya@example.com'},
    {'id' : 3, 'name': 'babitaji', 'email': 'babitaji@example.com'},
    {'id' : 4, 'name': 'champak chacha', 'email': 'champakchacha@example.com'},
    {'id' : 5, 'name': 'bhide', 'email': 'bhide@example.com'},
    {'id' : 6, 'name': 'sodhi', 'email': 'sodhi@example.com'}
]


def student_home(request):
    theme = request.GET.get('theme', 'light')

    if theme == 'dark':
        template_name = 'dark.html'
        current_css_theme = 'css/dark.css'
    else:
        template_name = 'light.html'
        current_css_theme = 'css/light.css'

    return render(request, template_name,{'current_css' : current_css_theme})

def student_list(request):
    return render(request, 'studentlist.html', context={'userData' : users})

def student_detail(request, studentid):
    return render(request, 'studentdetail.html', context={'student' : users[studentid-1]})


# def home(request): 
    theme = request.GET.get('theme', 'light')
    
    if theme == 'dark': 
        template = 'myapp/dark.html' 
        css = 'css/dark.css' 
    else: 
        template = 'myapp/light.html' 
        css = 'css/light.css' 
        
    return render(request, template, {'current_theme_css': css})
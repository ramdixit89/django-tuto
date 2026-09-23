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
    return render(request, 'studentHome.html')

def student_list(request):
    return render(request, 'studentlist.html', context={'userData' : users})

def student_detail(request):
    return render(request, 'studentdetail.html')
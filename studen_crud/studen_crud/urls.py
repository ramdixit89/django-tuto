from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.main_page, name='home'),
    path('login/', view.login_page, name='login'),
     path('register/', view.register_page, name='register'),
    path('student/list/', view.student_list),
    path('student/detail/<int:studentid>/', view.student_detail)
]
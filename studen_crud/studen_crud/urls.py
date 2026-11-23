from django.contrib import admin
from django.urls import path
from studen_crud import view
from register import views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.main_page, name='home'),
    path('login/', view.login_page, name='login'),
    path('register/', register_views.register_user, name='register'),
    path('student/list/', view.student_list, name='student_list'),
    path('student/list/<int:studentid>',view.delete_student, name="student_delete" ),
    path('student/detail/<int:studentid>/', view.student_detail, name='student_detail'),
    path('student/edit/<int:studentid>', view.edit_student, name="student_edit")
]

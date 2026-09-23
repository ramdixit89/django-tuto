from django.contrib import admin
from django.urls import path
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.student_home),
    path('student/list', view.student_list),
    path('student/detail', view.student_detail)
]

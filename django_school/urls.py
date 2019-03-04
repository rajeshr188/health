from django.urls import include, path
from django.contrib import admin
from classroom.views import classroom, students, teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
    path('select2/',include('django_select2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/doctor/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]

from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),

    path('patients/', include(([
        # path('quizlist/', students.QuizListView.as_view(), name='quiz_list'),
        path('', students.AppointmentListView.as_view(), name='appointment_list'),
        # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        path('appointment/create/', students.AppointmentCreateView.as_view(), name='appointment_create'),
        path('appointment/detail/<int:pk>/', students.AppointmentDetailView.as_view(), name='appointment_detail'),
    ], 'classroom'), namespace='students')),

    path('doctors/', include(([
        # path('quizlist/', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('', teachers.AppointmentListView.as_view(), name='appointment_list'),
        path('appointment/create/', teachers.AppointmentCreateView.as_view(), name='appointment_create'),
        path('appointment/detail/<int:pk>/', teachers.AppointmentDetailView.as_view(), name='appointment_detail'),

        path('symptom/', teachers.SymptomListView.as_view(), name='symptom_list'),
        path('symptom/create/', teachers.SymptomCreateView.as_view(), name='symptom_create'),
        path('symptom/detail/<int:pk>/', teachers.SymptomDetailView.as_view(), name='symptom_detail'),
        path('symptom/update/<int:pk>/', teachers.SymptomUpdateView.as_view(), name='symptom_update'),

        path('disease/', teachers.DiseaseListView.as_view(), name='disease_list'),
        path('disease/create/', teachers.DiseaseCreateView.as_view(), name='disease_create'),
        path('disease/detail/<int:pk>/', teachers.DiseaseDetailView.as_view(), name='disease_detail'),
        path('disease/update/<int:pk>/', teachers.DiseaseUpdateView.as_view(), name='disease_update'),

        path('feedback/', teachers.FeedBackListView.as_view(), name='feedback_list'),
        path('feedback/create/', teachers.FeedBackCreateView.as_view(), name='feedback_create'),
        path('feedback/detail/<int:pk>/', teachers.FeedBackDetailView.as_view(), name='feedback_detail'),
        path('feedback/update/<int:pk>/', teachers.FeedBackUpdateView.as_view(), name='feedback_update'),
        # path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        # path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        # path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        # path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        # path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]

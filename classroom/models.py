from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from django.urls import reverse

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


# class Subject(models.Model):
#     name = models.CharField(max_length=30)
#     color = models.CharField(max_length=7, default='#007bff')
#
#     def __str__(self):
#         return self.name
#
#     def get_html_badge(self):
#         name = escape(self.name)
#         color = escape(self.color)
#         html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
#         return mark_safe(html)
#
#
# class Quiz(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
#     name = models.CharField(max_length=255)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
#
#     def __str__(self):
#         return self.name
#
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
#     text = models.CharField('Question', max_length=255)
#
#     def __str__(self):
#         return self.text
#
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
#     text = models.CharField('Answer', max_length=255)
#     is_correct = models.BooleanField('Correct answer', default=False)
#
#     def __str__(self):
#         return self.text
#
#
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    #
    # def get_unanswered_questions(self, quiz):
    #     answered_questions = self.quiz_answers \
    #         .filter(answer__question__quiz=quiz) \
    #         .values_list('answer__question__pk', flat=True)
    #     questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
    #     return questions

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
        # Fields
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()

    # Relationship Fields
    doctor = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,related_name="apppat",
    )
    patient = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,related_name="appdoc",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('students:appointment_detail', args=(self.pk,))

    # def get_update_url(self):
    #     return reverse('students:appointment_update', args=(self.pk,))

class Symptom(models.Model):
      # Fields
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('teachers:symptom_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('teachers:symptom_update', args=(self.pk,))

class Disease(models.Model):
        # Fields
    name = models.CharField(max_length=130)

    # Relationship Fields
    symptom = models.ManyToManyField(
        'Symptom',
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('teachers:disease_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('teachers:disease_update', args=(self.pk,))

class FeedBack(models.Model):
      # Fields
    comment = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    # Relationship Fields
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name="patfeed",
    )
    doctor = models.ForeignKey(
        User,related_name="docfeed",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('teachers:feedback_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('teachers:feedback_update', args=(self.pk,))


# class TakenQuiz(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
#     score = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)
#
#
# class StudentAnswer(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

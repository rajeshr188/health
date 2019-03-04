from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django_select2.forms import Select2Widget,ModelSelect2Widget
from classroom.models import (
                              #   Answer, Question, Student, StudentAnswer,
                              # Subject,
                              User,Student,Appointment,Symptom,Disease,FeedBack)
import datetime
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user


# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }
#
#
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('text', )
#
#
class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


# class TakeQuizForm(forms.ModelForm):
#     answer = forms.ModelChoiceField(
#         queryset=Answer.objects.none(),
#         widget=forms.RadioSelect(),
#         required=True,
#         empty_label=None)
#
#     class Meta:
#         model = StudentAnswer
#         fields = ('answer', )
#
#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         super().__init__(*args, **kwargs)
#         self.fields['answer'].queryset = question.answers.order_by('text')

class AppointmentForm(forms.ModelForm):
    doctor=forms.ModelChoiceField(queryset=User.objects.filter(is_teacher=True),widget=Select2Widget)
    # date = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             # 'minDate': (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),  # Tomorrow
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #            'append': 'fa fa-calendar',
    #            'input_toggle': False,
    #            'icon_toggle': True,
    #         }
    #     ),
    # )

    class Meta:
        model = Appointment
        fields = ['date', 'doctor','patient',]

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['name']


class DiseaseForm(forms.ModelForm):
    symptom=forms.ModelMultipleChoiceField(queryset=Symptom.objects.all())
    class Meta:
        model = Disease
        fields = ['name', 'symptom']


class FeedBackForm(forms.ModelForm):
    patient=forms.ModelChoiceField(queryset=User.objects.filter(is_student=True),widget=Select2Widget)
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(is_teacher=True),widget=Select2Widget)
    class Meta:
        model = FeedBack
        fields = ['comment', 'patient', 'doctor']

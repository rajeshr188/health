from django.contrib import admin
from django import forms
from import_export import fields,resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import User,Appointment,Disease,Symptom,FeedBack
from import_export import resources

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass

# @admin.register(Disease)
# class DiseaseAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Symptom)
# class SymptomAdmin(admin.ModelAdmin):
#     pass
class DiseaseResource(resources.ModelResource):
    class Meta:
        model = Disease

class DiseaseAdminForm(forms.ModelForm):
    class Meta:
        model=Disease
        fields='__all__'

class DiseaseAdmin(ImportExportModelAdmin):
    form=DiseaseAdminForm
    resource_class=DiseaseResource
    list_display=('id','name')
admin.site.register(Disease, DiseaseAdmin)

class SymptomResource(resources.ModelResource):

    class Meta:
        model = Symptom

class SymptomAdminForm(forms.ModelForm):

    class Meta:
        model = Symptom
        fields = '__all__'

class SymptomAdmin(ImportExportModelAdmin):
    form = SymptomAdminForm
    resource_class=SymptomResource
    list_display=('id','name',)
admin.site.register(Symptom, SymptomAdmin)

from django.contrib import admin
from apiapp2.models import Student
# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','name','cls','school','Address']
admin.site.register(Student,AdminStudent)
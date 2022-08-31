from django.contrib import admin
from app.models import Student
# Register your models here.

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name','email','password')

# admin.site.register(Student,StudentAdmin)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']
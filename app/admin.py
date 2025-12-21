from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','task','created_date','updated_date','status']
    list_display_links = ['user']
    list_filter = ['created_date']
    ordering = ('-created_date',)


admin.site.register(Task,TaskAdmin)
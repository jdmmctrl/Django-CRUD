from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'datecompleted', 'important')
    list_filter = ('user', 'created', 'datecompleted', 'important')
    search_fields = ('title', 'description')
    readonly_fields = ('created', 'datecompleted')


# Register your models here.
admin.site.register(Task, TaskAdmin)

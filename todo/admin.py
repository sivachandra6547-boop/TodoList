from django.contrib import admin
from . models import Task

# Register your models her  e.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_created','updated_at')
    search_fields=('task',)
admin.site.register(Task,TaskAdmin)
 
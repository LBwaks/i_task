from django.contrib import admin
from .models import Assignees


# Register your models here.

@admin.register(Assignees)
class AssigneeAdmin(admin.ModelAdmin):
    list_display =['created_by','assignee','update_date']

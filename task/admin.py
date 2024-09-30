from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "priority",
        "status",
        "due_date",
        "assigned_to",
        "created_at",
    )
    search_fields = ("title", "priority", "status")
    list_filter = ("priority", "status", "due_date")

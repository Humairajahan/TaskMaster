from django.db import models


class Task(models.Model):
    HIGH = "HIGH"
    MEDIUM = "MED"
    LOW = "LOW"
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    PENDING = "PD"
    IN_PROGRESS = "IP"
    COMPLETED = "CO"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (IN_PROGRESS, "In Progress"),
        (COMPLETED, "Completed"),
    ]

    title = models.CharField(max_length=255)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default=LOW)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    assigned_to = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="tasks_assigned",
        related_query_name="assigned",
    )
    assigned_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="tasks_created",
        related_query_name="created",
    )

    class Meta:
        db_table = "task"

    def __str__(self):
        return self.title

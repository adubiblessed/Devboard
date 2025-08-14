from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        'base.User',    
        on_delete=models.CASCADE,
        related_name='tasks', 
        # remove default value when to push to production
        blank=True,
    )
    title = models.CharField(max_length=200, default='Untitled Task', blank=True)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"
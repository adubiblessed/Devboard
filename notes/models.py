from django.db import models

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(
        'base.User',    
        on_delete=models.CASCADE,
        related_name='notes',
    )
    title = models.CharField(max_length=200, default='Untitled Note', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
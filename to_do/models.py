from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo_text = models.CharField(max_length=400)
    added_date = models.DateTimeField()
    
    def __str__(self):
        return self.todo_text
    
    class Meta:
        verbose_name_plural = "To Do's"

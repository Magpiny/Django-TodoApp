from django.db import models

# Create your models here.
class TodoForm(models.Model):
    task = models.CharField(max_length=255, default="")
    mdate = models.DateField(default="")
    mtime = models.TimeField(default="")
    deadline = models.DateTimeField(default="")

    def __str__(self):
        return (self.task, self.mdate, self.mtime, self.deadline)      

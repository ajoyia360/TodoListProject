from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # Define choices for categories
    CATEGORY_CHOICES = (
        ('work', 'Work'),
        ('study', 'Study'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

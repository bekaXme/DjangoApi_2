from django.db import models

# Create your models here.
class PythonMaterial(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=100, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Tab1(models.Model):
    url=models.CharField(max_length=50)
    time=models.DateTimeField()
    verified=models.BooleanField()
    image=models.ImageField(upload_to="pic")

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


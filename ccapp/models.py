from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=200)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question_text

class ApplicantStatus(models.Model):
    class Meta:
        verbose_name_plural = "Applicant Statuses"
        
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Applicant(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField(blank=False)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    motivation_letter = models.TextField(max_length=1000)
    status = models.ForeignKey(ApplicantStatus, on_delete=models.CASCADE, default=3)
    photo = models.FileField(upload_to='static/applicant_photos', blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    message_text = models.CharField(max_length=1000)
    sender_name = models.CharField(max_length=30)
    sender_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.sender_name

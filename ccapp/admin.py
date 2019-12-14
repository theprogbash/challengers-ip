from django.contrib import admin
from .models import Question, Applicant, Message, ApplicantStatus
from django.contrib.auth.models import Group, User

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer')

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date', 'phone', 'email', 'motivation_letter', 'status', 'photo')

class ApplicantStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'message_text', 'sender_email')

admin.site.site_header = "Challengers Club - Admin Dashboard" 
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ApplicantStatus, ApplicantStatusAdmin)
admin.site.register(Message, MessageAdmin)
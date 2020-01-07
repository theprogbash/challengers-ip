from django.contrib import admin
from .models import Question, Applicant, Message, ApplicantStatus
from django.contrib.auth.models import Group, User
from django.http import HttpResponse

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) 
    
    writer.writerow([
        smart_str(u"Ad"),
        smart_str(u"Soyad"),
        smart_str(u"Doğum tarixi"),
        smart_str(u"Telefon"),
        smart_str(u"Elektron Poçt"),
        smart_str(u"Motivasiya Məktubu"),
        smart_str(u"Status"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.name),
            smart_str(obj.surname),
            smart_str(obj.birth_date),
            smart_str(obj.phone),
            smart_str(obj.email),
            smart_str(obj.motivation_letter),
            smart_str(obj.status),
        ])
    return response
export_csv.short_description = u"Export CSV"

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer')

class ApplicantAdmin(admin.ModelAdmin):
    actions = [export_csv]
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
# admin.site.register(ApplicantStatus, ApplicantStatusAdmin)
admin.site.register(Message, MessageAdmin)
from django.shortcuts import render
from .models import Question, Applicant, Message
from django.core.mail import send_mail
from django.conf import settings


def index(request): 
    context = {
        'questions': Question.objects.all(),
        'applicants':  Applicant.objects.filter(status=1),
        'empty_cards': range(4 - Applicant.objects.filter(status=1).count())
    }
    if request.method == "POST":
        if request.POST.get('motivation_letter'):
            Applicant.objects.create(
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            birth_date = request.POST.get('birth_date'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            motivation_letter = request.POST.get('motivation_letter'))
        
        if request.POST.get('message_text'):
            Message.objects.create(
                sender_name = request.POST.get('sender_name'),
                sender_email = request.POST.get('sender_email'),
                message_text = request.POST.get('message_text'))

    if request.method == 'POST':
        sender_email = request.POST.get('sender_email')
        sender_name = request.POST.get('sender_name')
        subject = 'Challengers Club-a xoş gəldin !'
        message = 'Hörmətli ' + str(sender_name) + '! \nMüraciətiniz üçün təşəkkür edirik. Tezliklə sualınız cavablandırılacaq.'
        from_email = settings.SERVER_EMAIL
        recipient_list = [sender_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    if request.method == 'POST':
        if request.POST.get('motivation_letter'):
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            email = request.POST.get('email'),
            from_email = settings.SERVER_EMAIL
            subject = 'Challengers Club-a xoş gəldin !'
            message = 'Hörmətli ' + str(name) + ' ' + str(surname) + '! \nMüraciətiniz üçün təşəkkür edirik. Tezliklə sizə geri dönüş edəcəyik.'
            from_email = settings.SERVER_EMAIL
            recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return render(request, 'index.html', context)

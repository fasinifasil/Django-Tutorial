from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
def EmailSendFunction(request):

    send_mail('Django Mailsent','Email Send Please check Automic created msg','djangopython2024@gmail.com',recipient_list=['fasinifasil@gmail.com','djangopython2024@gmail.com'],fail_silently=False)
    return render(request,'MailSend.html')



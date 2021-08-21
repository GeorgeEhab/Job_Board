from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# Created By Me
def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']  # request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # print(subject);print(email);print(message)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # send from
            [email],                   # to
        )
    page_template = 'contact/contact.html'
    context = {'myinfo':myinfo}
    return render(request,page_template,context)

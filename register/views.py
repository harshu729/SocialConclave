from django.shortcuts import render
from core.models import Member
from .forms import *
from SocialConclave.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
from django.views.generic import TemplateView

# Create your views here.

class Registration(TemplateView):
    def get(self,request):
        form = DelegateForm()
        return render(request, 'register/register.html', {'form': form})
    def post(self,request):
        form = DelegateForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name') 
            recepient = str(form['email'].value())
            mail_content_delegate = f"""
                <html>
                    <body>
                        <p>Thanks for registering</p>
                    </body>
                </html>
            """
            mail_content_treasurer = f"""
                <html>
                    <body>
                        <p>{name} has registered.</p>
                    </body>
                </html>
            """
            msg_dele = EmailMessage(f'Thanks for Registering, {name}!',mail_content_delegate, EMAIL_HOST_USER, [recepient])
            msg_tr = EmailMessage(f'{name} has registered',mail_content_treasurer,EMAIL_HOST_USER,['poorvachadha.nmims@gmail.com'])
            msg_dele.content_subtype =  'html'
            msg_tr.content_subtype = 'html'
            msg_dele.send()
            msg_tr.send()
            # subject = 'hi deer'
            # message = 'Hope you are enjoying your Django Tutorials'
            # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request,'main/index.html',{'recepient':recepient})
                
def home(request):
    form = DelegateForm()
    return render(request, 'register/register.html', {'form': form})

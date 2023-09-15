from django.shortcuts import render,redirect
from .models import Project
from django.core.mail import send_mail 
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.
@csrf_protect
def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    if request.method == 'POST':
        username = request.POST.get('name')
        email_address = request.POST.get('email')
        message = request.POST.get('message')

        if username == "" or email_address == "" or message == "":
            messages.warning(request, "One or more fields are empty!")
            return redirect('home') 

        data = {
            'username': username,
            'email_address': email_address,
            'message': message
        }

        email_subject = 'Contact Form from Website'
        email_message = f'''
        New message: {data['message']}
        From: {data['email_address']}
        '''

        try:
            send_mail(email_subject, email_message,'settings.EMAIL_HOST_USER',[data['email_address']], fail_silently=False)
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending the message: {str(e)}")
    return render(request, 'base/index.html', context)

def main_screen(request):
    return render(request, 'base/main_sc.html')

def about(request):
    return render(request, 'base/about.html')
 
def services(request):
    return render(request, 'base/services.html')   

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'base/project_detail.html', {'project': project})


def contact_us(request):
    return render(request, 'base/contact_us.html')

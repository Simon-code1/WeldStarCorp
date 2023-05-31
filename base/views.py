from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail 
from django.shortcuts import render, get_object_or_404


# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
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
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            "Subject"+ message_name,
            message,
            "From:" + message_email,
            ['sdychka@rogers.com'],
        )
         
        return render(request, 'base/contact_us.html', {'name','email','message'})
    else:
        return render(request, 'base/contact_us.html', {})    
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/#contact-section')  # redirects back to contact section

    return render(request, 'index.html')
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def contact(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        message=request.POST['message']
        email=request.POST['email']

        # Check if enquiry is made


        contact = Contact(first_name=first_name, last_name=last_name, message=message, email=email,)
        contact.save()
        messages.success(request, "Your feedback has been submitted to the concerned one")
        from_email=request.user.email
        send_mail(first_name, message,from_email, ['koiralasagar138@gmail.com'])
        return redirect('contact')



    else:
        return render(request,'contact/contact.html')

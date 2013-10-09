'''
Created on 09.10.2013

@author: mga
'''
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def contact_form(request):
    return render(request, 'contact_form.html')

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append("Enter a subject.")
        if not request.POST.get('message'):
            errors.append("Enter a message.")
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append("Enter a valid e-mail address.")
        if not errors:
            send_mail(request.POST['subject'], \
                      request.POST['message'], 
                      request.POST.get('email', 'noreply@example.com'), 
                      ['siteowner@example.com'])   
            return HttpResponseRedirect('/contact/thanks')
    return render(request, 'contact_form.html', {'errors': errors})  

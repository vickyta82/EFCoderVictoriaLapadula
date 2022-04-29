from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context

def user_registration (request):
    user_registration = open(r"C:\Users,\vlapa\Desktop\Python\EFCoderVicky\FinalProject\Blog\templates\Blog\user_registration.html", 'r')
    template2 = Template(user_registration.html.read())
    user_registration.html.close()
    context = Context()
    doc2 = template2.render(context)
    return HttpResponse(doc2)

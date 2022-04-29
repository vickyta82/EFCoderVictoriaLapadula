from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from Blog.forms import Post
from Blog.models import *

def home(request):
    return render(request, "Blog/index.html")

def user_login (request):
    user_login = open(r"C:\Users,\vlapa\Desktop\Python\EFCoderVicky\FinalProject\Blog\templates\Blog\user_login.html", 'r')
    template3 = Template(user_login.html.read())
    user_login.html.close()
    context = Context()
    doc1 = template3.render(context)
    return HttpResponse(doc1)


def user_registration (request):
    user_registration = open(r"C:\Users,\vlapa\Desktop\Python\EFCoderVicky\FinalProject\Blog\templates\Blog\user_registration.html", 'r')
    template2 = Template(user_registration.html.read())
    user_registration.html.close()
    context = Context()
    doc2 = template2.render(context)
    return HttpResponse(doc2)

def create_post (request):
    form = Post()
    if request.method == "POST": 
        form = Post(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user_post = post(post=data['post'],author=data['author'], img=data["img"], title=data["title"], subtitle=data["subtitle"])
            user_post.save()
            return redirect('Post')
        else:
            return render(request, 'Blog/create_post.html', {'formulario': form})
     
    else : 
        print("GET")
        context = {"formulario": form}
        doc3 = render(request, "Blog/create_post.html", context)
        return HttpResponse(doc3)

def post_view (request):
    posts = post.objects.all()
    no_posts = True
    if len(posts) > 0:
        no_posts = False
    return render(request, 'Blog/post.html', {"posts": posts, "no_posts": no_posts})

def page_detail(request, id):
    post_found = post.objects.filter(id = id).first()
    return render(request, 'Blog/fullpost.html', {"post": post_found})

def about(request):
    return render(request, 'Blog/about.html')

def Links(request):
    return render(request, 'Blog/links.html')    

def Tutorials(request):
    return render(request, 'Blog/tutorials.html') 
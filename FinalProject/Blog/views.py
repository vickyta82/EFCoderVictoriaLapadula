from django.shortcuts import render, redirect
from django.http import HttpResponse
from Blog.forms import Post, ChatForm
from Blog.models import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "Blog/index.html")

@login_required
def create_post (request):
    form = Post()
    if request.method == "POST": 
        form = Post(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user_post = post(post=data['post'],author=data['author'], img=data["img"], title=data["title"], subtitle=data["subtitle"], user=request.user)
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

@login_required
def update_post(request, id):
    print(id)
    postFinded = post.objects.filter(id = id).first()
    if request.method == 'POST':
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            existent_post = post.objects.filter(id = id)
            if len(existent_post)>0:
                existent_post = existent_post[0]
                existent_post.title = data["title"]
                existent_post.subtitle = data["subtitle"]
                existent_post.img = data["img"]
                existent_post.post = data["post"]
                existent_post.author = data["author"]
                existent_post.save()
            return redirect('Post')
        else:
            return render(request, 'Blog/create_post.html', {'formulario': form})
    else:
        if postFinded:
            form = Post({"title":postFinded.title,"subtitle":postFinded.subtitle, "image": postFinded.img, "post": postFinded.post, "author": postFinded.author})
            return render(request, 'Blog/create_post.html', {'formulario': form})
        else:
            return redirect('Post')

@login_required
def remove_post(request, id):
    try:
        postFinded = post.objects.get(id = id)
        postFinded.delete()
        return redirect('Post')
    except Exception as e:
        print(e)
        return redirect('Post')

def page_detail(request, id):
    post_found = post.objects.filter(id = id).first()
    return render(request, 'Blog/fullpost.html', {"post": post_found})

def about(request):
    return render(request, 'Blog/about.html')

def Links(request):
    return render(request, 'Blog/links.html')    

def Tutorials(request):
    return render(request, 'Blog/tutorials.html') 

@login_required
def chat (request):
    chat_form = ChatForm()
    chat = Chat.objects.all()
    if request.method == 'POST':
        chat_form_content = ChatForm(request.POST)
        if chat_form_content.is_valid():
            data = chat_form_content.cleaned_data
            chat = Chat(chat=data["chat"], user=request.user)
            chat.save()
            return redirect('Chat')
        else:
            return render(request, 'Blog/chat.html', {"chat_form": chat_form_content, "chat": chat})
    else:
        return render(request, 'Blog/chat.html', {"chat_form": chat_form, "chat": chat})
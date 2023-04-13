from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts':posts})

def post(request, pk):
  posts = Post.objects.get(id=pk)
  return render(request, 'post.html', {'posts':posts})

def addblog(request):
  return render(request, 'addblog.html')

def addblogdisplay(request):
  title = request.GET['title']
  body = request.GET['description']
  posts = Post.objects.create(title=title, body=body)
  posts.save()
  return redirect('index')

def deleteblog(request):
  return render(request, 'deleteblog.html')

def deleteblogdisplay(request):
  title = request.GET['title']
  if Post.objects.filter(title=title).exists():
    posts = Post.objects.get(title=title)
    posts.delete()
    return redirect('index')
  else:
    messages.info(request,'Blog with this title does not exist')
    return redirect('deleteblog')


from django.shortcuts import render,redirect
from .forms import PostUpdateForm

from .models import Post
# Create your views here.

def index(request):
    posts= Post.objects.all()
    return render(request, 'index.html',{"posts":posts})

def post(request):
    
    if request.method == "POST":
        form=PostUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=PostUpdateForm
  
    return render(request,"post.html",{"form":form})

    

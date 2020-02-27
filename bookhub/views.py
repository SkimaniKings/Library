from django.shortcuts import render,redirect
from .forms import PostUpdateForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def post(request):
    
    if request.method == "POST":
        form=PostUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=PostUpdateForm
  
    return render(request,"post.html",{"form":form})
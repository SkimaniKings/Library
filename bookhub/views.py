from django.shortcuts import render,redirect
from .forms import PostUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'index.html')

# def post(request):
    
#     if request.method == "POST":
#         form=PostUpdateForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form=PostUpdateForm
  
#     return render(request,"post.html",{"form":form})
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post.html'
    fields = ['title', 'image','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
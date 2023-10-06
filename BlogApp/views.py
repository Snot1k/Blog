from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
# Create your views here.
def index(req):
    post_list = Post.objects.all()
    return render(request=req, template_name="blogapp/index.html", context={"posts" : post_list})
#create class for view post
class PostDetailView(DetailView):
    template_name = "blogapp/post-detail.html"
    
    model=Post

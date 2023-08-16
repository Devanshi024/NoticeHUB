
from django.template.defaultfilters import slugify
from .models import *
from .forms import *
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages


    
# def edit_post(request, id):
#     post = get_object_or_404(postmodel, id=id)

#     if request.method == 'GET':
#         context = {'form': postmodel(instance=postmodel), 'id': id}
#         return render(request,'notice/index.html',context)

# other functions


# Create your views here.
def index(request):
    # for accessing single object in django
    # posts = postmodel.objects.get(title='NewNoticee')
    # print(posts.id)
    # print(posts.image.url)
    # print(p['image'])

    posts = postmodel.objects.all()

   
    if request.method == 'POST':
        form = PostModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Notice')
    else:
         form = PostModelForm()
       
    context ={
        'posts' : posts,
        'form' : form,
    }
    return render(request,'notice/index.html',context)
    


def aboutus(request):
    return render(request,'notice/aboutus.html')

def post_detail(request, pk):
    posts = postmodel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('blog-post-detail', pk=posts.id)
    else:
         form = PostModelForm()
       
    context ={
        'posts' : posts,
        'form' : form,
    }
    return render(request,'notice/index.html',context)
    

def post_edit(request, pk):
    posts = postmodel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
        return redirect('blog-post-detail', pk=posts.id)
    else:
        form = PostUpdateForm(instance=posts)
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'notice/post_edit.html', context)

def post_delete(request, pk):
    post = postmodel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('Notice')
    context = {
        'post': post
    }
    return render(request, 'notice/post_delete.html', context)









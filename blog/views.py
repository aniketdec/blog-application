from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created")
            username=form.cleaned_data.get('username')
            return redirect('blog-home')  
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})
class post():
    def __init__(self,author,title,content,avatar,posted_on,url):
        self.author=author
        self.url=url
        self.title=title
        self.content=content
        self.avatar=avatar
        self.posted_on=posted_on
def home(request):
    d={}
    profile=Profile.objects.all()
    url=''
    for i in profile:
        d.update({i.user.id:[i.user.username,i.avatar]})
    b=Post.objects.all()
    l=[]
    print (d)
    for i in b:
        print (i.author)
        url='/user/profile'+str(i.author)+"/"
        t=post("      "+d[i.author][0],i.title,i.content,d[i.author][1],i.posted_on,url)
        l.append(t)
    l=l[::-1]
    return render(request,'blog/home.html',{'blogs':l})
def addblog(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        avatar=''
        p=Profile.objects.all()
        if form.is_valid():
            post=form.save(commit=False)
            blog=Post(title=form.cleaned_data.get('title'),content=form.cleaned_data.get('content'),posted_on=timezone.now(),author=request.user.id)
            blog.save()
            return redirect('home')  
    else:
        form=PostForm()
    return render(request,'blog/addblog.html',{'form':form})
'''def like(request, picture_id):
    new_like, created = Like.objects.get_or_create(user=request.user, picture_id=picture_id)
    if not created:
        # the user already liked this picture before
    else:
        # oll korrekt'''
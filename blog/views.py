from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Post,BlogComment
# Create your views here.
def blogpage(request):
      allPosts=Post.objects.all()
      context={"allPosts":allPosts}
      return render(request,"blog/blogpage.html",context)

def blogpost(request,slug):
      post=Post.objects.filter(slug=slug).first()
      comments=BlogComment.objects.filter(post=post,parent=None)
      replies=BlogComment.objects.filter(post=post).exclude(parent=None)
      replyDict={}
      for reply in replies:
            if reply.parent.sno not in replyDict:
                  replyDict[reply.parent.sno]=[reply]
            else:
                  replyDict[reply.parent.sno].append(reply)
      print(replyDict)
      context={'post':post,'comments':comments , 'user': request.user, 'replyDict':replyDict}
      return render(request,'blog/blogpost.html',context)
    
def postComment(request):
      if request.method == 'POST':
            comment=request.POST['comment']
            user=request.user
            postno=request.POST['postno']
            post=Post.objects.get(sno=postno)
            parentSno=request.POST.get('parentSno')
            if parentSno == "":

                  mycomment=BlogComment(comment=comment, user=user, post=post)
                  mycomment.save()
                  messages.success(request,"Your comment has been posted successfully")
            else:
                  parent=BlogComment.objects.get(sno=parentSno)
                  mycomment=BlogComment(comment=comment, user=user, post=post, parent=parent)
                  mycomment.save()
                  messages.success(request,"Your reply has been posted sucessfully")

      return redirect(f"/blog/{post.slug }")
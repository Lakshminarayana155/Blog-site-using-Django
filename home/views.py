from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
      return render(request,'home/home.html')
#     return HttpResponse("This is HOME page")

def about(request):
      return render(request,'home/about.html')
      
#       return HttpResponse("This is ABOUT page")

def contact(request):
      if request.method == 'POST':
            name=request.POST["name"]
            email=request.POST["uemail"]
            phone=request.POST['phoneno']
            content= request.POST['comment']
            if len(name)<3 or len(email)<3 or len(phone)<10 :
                  messages.error(request,"!Invalid Credentials Please fill the form correctly")
            else:
                  contact= Contact(name=name, email=email, phone=phone, content=content)
                  contact.save()
                  messages.success(request,"Your response has been submiteed sucessfully")
      return render(request,'home/contact.html')

        # return HttpResponse("This is CONTACT page")

def search(request):
      query=request.GET['query']
      if len(query)>70:
            allPosts=Post.objects.none()
      else:
            allPosts=Post.objects.filter(title__icontains=query)
            allPosts=Post.objects.filter(author__icontains=query)
            allPosts=Post.objects.filter(content__icontains=query)
      if allPosts.count()==0:
            messages.warning(request,"No search results found. Please refine your query")

      context={"allPosts":allPosts,
               'query':query}
      return render(request,'home/search.html',context)

def blogSignin(request):
      if request.method =="POST":
            #parameters
            inputuname=request.POST["inputuname"]
            inputfname=request.POST["inputfname"]
            inputlname=request.POST["inputlname"]
            inputemail=request.POST["inputemail"]
            inputPassword1=request.POST["inputPassword1"]
            inputPassword2=request.POST["inputPassword2"]
            
            #checking pass
            if len(inputuname)>10:
                  messages.error(request,"Username must be less than 10 characters!")
                  return redirect("home")
            
            if not inputuname.isalnum():
                  messages.error(request,"Username should only contain letter and numbers!")
                  return redirect("home")

            if inputPassword1 != inputPassword2:
                  messages.error(request,"Passwords do not match")
                  return redirect("home")

            #creating user
            myuser= User.objects.create_user(inputuname,inputemail,inputPassword1)
            myuser.first_name=inputfname
            myuser.last_name=inputlname
            myuser.save()
            messages.success(request,"Your account has been created sucessfully")
            return redirect('home')
      else:
            return HttpResponse("Error please try again")
      
def blogLogin(request):
      if request.method == "POST":
            loginUname=request.POST["loginUname"]
            loginUpass=request.POST["loginUpass"]

            user = authenticate(username=loginUname,password=loginUpass)

            if user :
                  login(request, user)
                  messages.success(request,"Sucessfully Logged In")
                  return redirect("home")
            else:
                  messages.error(request,"Invalid credentials, Please check and retry")
                  return redirect("home")
      return HttpResponse("404 - Not Found")

def blogLogout(request):
      logout(request)
      messages.success(request,"Sucessfully Logged Out")
      return redirect('home')

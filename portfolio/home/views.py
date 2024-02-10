from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
     context={
          'name':'monika',
          'course':'bca'
     }
     return render(request,'home.html',context)
def about(request):
     return render(request,'about.html')
def projects(request):
     return render(request,'projects.html')
def contact(request):
     miss=""
     if request.POST.get('name')=='':
            return render(request,"contact.html",{'error':True, 'miss':"you have missed your name,please try again! "})
     if request.POST.get('email')=='':
            return render(request,"contact.html",{'error':True,'miss':"you have  missed your email,please try again!  "})
     if request.POST.get('phone')=='':
            return render(request,"contact.html",{'error':True,'miss':"you have  missed your  phone number,please try again!"})
     if request.POST.get('desc')=='':
            return render(request,"contact.html",{'error':True,'miss':"you have   missed your desc,please try again!"})
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          ins=Contact(name=name,email=email,phone=phone,desc=desc)
          ins.save()
          print("data has been witten to the db")
     return render(request,'contact.html')

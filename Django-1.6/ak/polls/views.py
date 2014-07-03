from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from Hr_Management_Tool_DB import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect


from django.core.mail.message import EmailMessage

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from smtplib import SMTP

@csrf_exempt
def signInB(request):
    ID=request.POST["username"]
    print ID
    paswd = request.POST["Password"]
  
    dB = DataBase()
    x=dB.search(ID,paswd)
    print x
    if(x==1):
        
        return render(request,'Thankyou.html',{})
    else:
        return render(request,'Forgotpassword.html',{})

@csrf_exempt
def signinmethod(request):
    
    x=12
    print x

    return render(request,'check1.html',{})
@csrf_exempt
def forgetPasswordPageShow(request):
    
    return  render(request,'Forgotpassword.html',{})
@csrf_exempt
def signUp(request):
    
    return  render(request,'signup.html',{})
@csrf_exempt
def Check(request):
    ID=request.POST["username"]
    print ID
    
    dB = DataBase()
    listOfList=dB.Check1(ID)
    
   
    return render(request,'Thankyou.html',{'listOfList':listOfList})
@csrf_exempt
def Check2(request):
    ID=request.POST["username"]
    print ID
    dB = DataBase()
    listOfList1=dB.Check3(ID)
    #return render(request,'Thankyou.html',{'listOfList1':listOfList1})
    return render(request,'Thankyou.html',{})

def submit(request):
    ID=request.POST["userName"]
    print ID
    paswd = request.POST["password"]
    print paswd
    s=request.POST["sex"]
    print s
    s1=request.POST["datepicke1"]
    dB = DataBase()
    x=dB.submitSignIn1(ID,paswd,s,s1)
    return  render(request,'sub.html',{})
@csrf_exempt
def option1(request):
    ID=request.POST["username"]
    print ID
    paswd = request.POST["Password"]
    print paswd
    
    dB = DataBase()
    dB.update(ID,paswd)
    return render(request,'chpass.html',{})

def redirect(request):
    return  render(request,'email.html',{})

from django.core.mail import send_mail

def emailsend1(request):	  
	
    val=request.POST['emailid']
    print val
    text=request.POST['msg']
    print text
    
    email11 = EmailMessage('content ', 'Your content - ' +text,  'brisatechnology@gmail.com', [val],None,None,None,None,[])
    email11.send()

   
    
    return render(request,'emailthanks.html',{})



def forget1(request):
    return render(request,'forget1.html',{})

def forgetmethod(request):	  
	
    val=request.POST['emailid']
    print val
    val1="1adsad12"
    user=request.POST['username']
    dB = DataBase()
    dB.update(user,val1)
    val1="1adsad12"
    email11 = EmailMessage('content ', 'Your password - '+val1,  'brisatechnology@gmail.com', [val],None,None,None,None,[])
    email11.send()

   
    
    return render(request,'passwordthanks.html',{})
    

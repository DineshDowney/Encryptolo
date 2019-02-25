from django.shortcuts import render
from encryptolo import forms
from encryptolo import Encryption as enc
from encryptolo import Decryption as dnc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create your views here.
def index(request):
    return render(request,"index.html")

def sendmail(receiver, key,x):
    fromaddr = "xoxo@dineshgarg.co"
    toaddr = receiver

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Your Key and Text"

    body = "Encrypted Text is: \n\n" + x + "\n\n\nand your Key is \n\n" + key

    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "nososmart")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def FormFun(request):
    FormObj = forms.FormClass()
    x=""
    y=""
    Email=""
    if request.method=='POST':
        FormObj=forms.FormClass(request.POST)
        if FormObj.is_valid():
            Email=FormObj.cleaned_data['Email']
            para_1=FormObj.cleaned_data['text']
            x,y=enc.fun(para_1)
            sendmail(Email, y,x)
    context = {'form_dic1':FormObj, 'x': x, 'y':y}
    return render(request,"form_1.html",context)


def FormFun2(request):
    FormObj2=forms.FormClass2()
    x=""
    if request.method=='POST':
        FormObj2=forms.FormClass2(request.POST)
        
        if FormObj2.is_valid():
            para_2=FormObj2.cleaned_data['key']
            para_1=FormObj2.cleaned_data['dec_text']
            x=dnc.fun(para_1,para_2)
    context={'form_dic2':FormObj2, 'x': x}
    return render(request,"form_2.html",context)

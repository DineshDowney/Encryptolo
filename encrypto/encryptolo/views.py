from django.shortcuts import render
from encryptolo import forms
from encryptolo import Encryption as enc
from encryptolo import Decryption as dnc
import os
# Create your views here.
def index(request):
    return render(request,"index.html")

def FormFun(request):
    FormObj = forms.FormClass()

    if request.method=='POST':
        FormObj=forms.FormClass(request.POST)
        x="_____"
        if FormObj.is_valid():
            FormObj.cleaned_data['name']
            para_1=FormObj.cleaned_data['text']
            os.system('python '+ os.getcwd() + '\encryptolo\Encryption.py ' + para_1)
            x,y=enc.fun(para_1)
    context = {'form_dic1':FormObj, 'x': x, 'y':y}
    return render(request,"form_1.html",context)


def FormFun2(request):
    FormObj2=forms.FormClass2()
    x="_____"
    if request.method=='POST':
        FormObj2=forms.FormClass2(request.POST)
        
        if FormObj2.is_valid():
            para_2=FormObj2.cleaned_data['key']
            para_1=FormObj2.cleaned_data['dec_text']
            #os.system('python '+ os.getcwd() + '\encryptolo\Decryption.py ' + para_1 + ' ' + para_2)
            x=dnc.fun(para_1,para_2)
    context={'form_dic2':FormObj2, 'x': x}
    return render(request,"form_2.html",context)

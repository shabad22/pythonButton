from django.shortcuts import render
import requests
def button(request):
    return render(request,'home.html')
def addition(request):
    a = 5
    b = 5
    c = a+b
    return render(request,'home.html',{'add':c})
def output(request):
    data=requests.get("https://reqres.in/api/users")
    # print(data.text) 
    data=data.text
    return render(request,'home.html',{'keyData':data})
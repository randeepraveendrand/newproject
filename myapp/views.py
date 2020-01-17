from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def mycss(request):
    return render(request,'css.html')

def checkt(request):
    return render(request,'check.html')    

def hello(request):
    return render(request,'hello.html')
    
def last(request):
    return render(request,'last.html')    
def color(request):
    return render(request,'color.html')  

def btas1(request):
    return render(request,'btsasgn1.html') 
def btas2(request):
    return render(request,'btsasgn2.html')
def btas3(request):
    return render(request,'btsasgn3.html')

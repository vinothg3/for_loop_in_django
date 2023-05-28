from django.shortcuts import render

# Create your views here.
def forloop(request):
    a=[1,2,3,4,5,6]
    d={'a':a}
    
    return render(request,'forloop.html',d)

def setsqu(request):
    s={1,5,6,7,8}
    d={'s':s}
    return render(request,'setsqu.html',d)


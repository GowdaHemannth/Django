from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "Name":"Steve-Rogers"
    }
    return render(request,'index.html',context)
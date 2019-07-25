from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def minji(request):
    return render(request, 'minji.html')
    
def gaeun(request):
    return render(request, 'gaeun.html')
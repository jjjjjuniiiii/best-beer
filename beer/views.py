from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'beer/index.html',{})

def list(request):
	return render(request, 'beer/list.html',{})

def write(request):
	return render(request, 'beer/write.html',{})

def login(request):
	return render(request, 'beer/login.html',{})
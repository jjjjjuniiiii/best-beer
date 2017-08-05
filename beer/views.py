from django.shortcuts import render
from django.utils import timezone
from .models import Beer

# Create your views here.
def index(request):
	beers = Beer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'beer/index.html', {'beers': beers})
	
def about(request):
	return render(request, 'beer/about.html',{})

def beer_listing(request):
	return render(request, 'beer/beer-listing.html',{})

def beer_details(request):
	return render(request, 'beer/beer-details.html',{})

def contact(request):
	return render(request, 'beer/contact.html',{})

def write(request):
	return render(request, 'beer/write.html',{})

def login(request):
	return render(request, 'beer/login.html',{})
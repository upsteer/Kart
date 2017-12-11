from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	context = {
		"title": "Home",
		"content": "Welcome to the homepage."
	}
	return render(request, "home_page.html", context)


def about_page(request):
	context = {
		"title": "About",
		"content": "This is the about page."
	}
	return render(request, "home_page.html", context)


def contact_page(request):
	context = {
		"title": "Contact",
		"content": "This is the contact page."
	}
	return render(request, "home_page.html", context)


def home_page_old(request):
	return HttpResponse("<h1>Hello World!</h1>")

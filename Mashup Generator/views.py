# views.py
from django.shortcuts import render

def home(request):
    page_title = "Home Page"
    page_content = "Welcome to the Mashup Generator Web App"
    return render(request, "home.html", {"page_title": page_title, "page_content": page_content})
from django.shortcuts import render     #imported by default
from django.views.generic import ListView   #to display lists
from .models import Book                #to access Book model

# Create your views here.
class BookListView(ListView):           #class-based view
   model = Book                         #specify model
   template_name = 'books/main.html'    #specify template 

def home(request):
    return render(request, 'books/books_home.html')
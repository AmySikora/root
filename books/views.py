from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Book 
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin                               #to access Book model

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
#class-based “protected” view                              #class-based view
   model = Book  
#specify model                                          #specify model
   template_name = 'books/main.html'                    #specify template

class BookDetailView(LoginRequiredMixin, DetailView):                     #class-based view
   model = Book                                        #specify model
   template_name = 'books/detail.html'  
   
def home(request):
    return render(request, 'books/books_home.html')               #specify template

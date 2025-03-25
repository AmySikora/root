from django.shortcuts import render
#to protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

def records(request):
   #do nothing, simply display page    
   return render(request, 'sales/records.html')

#define function-based view - records()
def records(request):
   #create an instance of SalesSearchForm that you defined in sales/forms.py
   form = SalesSearchForm(request.POST or None)

   #check if the button is clicked
   if request.method =='POST':
       #read book_title and chart_type
       book_title = request.POST.get('book_title')
       chart_type = request.POST.get('chart_type')
       #display in terminal - needed for debugging during development only
       print (book_title, chart_type)


   #pack up data to be sent to template in the context dictionary
   context={
           'form': form,
   }

   #load the sales/record.html page using the data that you just prepared
   return render(request, 'sales/records.html', context)
#keep protected
@login_required
def records(request):
   #do nothing, simply display page    
   return render(request, 'sales/records.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm

def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        print(book_title, chart_type)  # Optional: Debugging only

    context = {
        'form': form,
    }

    return render(request, 'sales/records.html', context)

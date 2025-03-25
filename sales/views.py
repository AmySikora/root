from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale, Book  # Make sure Book is imported
import pandas as pd

# Utility function to get book name from book_id
def get_bookname_from_id(val):
    book = Book.objects.get(id=val)
    return book.name

def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None

    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')

        # Filter sales based on book title
        qs = Sale.objects.filter(book__name=book_title)

        if qs.exists():
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            sales_df = sales_df.to_html()

        # Debugging info
        print(f"Book Title: {book_title}, Chart Type: {chart_type}")
        print("QuerySet:", qs)
        print("Values:", qs.values())

        try:
            obj = Sale.objects.get(id=1)
            print("Sample Sale Object:", obj)
        except Sale.DoesNotExist:
            print("Sale with id=1 does not exist.")

    context = {
        'form': form,
        'sales_df': sales_df,
    }

    return render(request, 'sales/records.html', context)

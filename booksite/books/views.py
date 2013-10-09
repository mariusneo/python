from django.shortcuts import render
from django.http import HttpResponse
from models import Book
import datetime
from django.http.response import Http404
 

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render(request, 'latest_books.html', {'book_list': book_list}) 

def hello(request):
    return HttpResponse("Hello World")

def current_date(request):
    current_date = datetime.datetime.now()
    return render(request, 'current_date_time.html', {'current_date':current_date})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html', {'books':books, 'query':q})
    else:
        # message = 'You submitted an empty form.'
        return render(request, 'search_form.html', {'error': True})

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
# def index(request):
#     return render(request, 'polls/starter.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'polls/home.html',
        {
            'title':'Home Page',
        }
    )

def contact(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'polls/contact.html',
        {
            'title':'contact Page',
        }
    )
from django.shortcuts import render

def index(request):
    """
    Method which will render index page which will show the live rates in every minute
    """
    
    return render(request, "main/index.html")


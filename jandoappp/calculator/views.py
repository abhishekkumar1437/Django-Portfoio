from django.shortcuts import render
import urllib.request
# Create your views here.
def calculator(request):
    return render(request,"calculators.html")
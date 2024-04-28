from django.shortcuts import render, HttpResponse

# Create your views here.
def signIn(request):
    return render(request, "signIn.html")
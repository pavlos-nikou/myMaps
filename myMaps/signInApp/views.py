from django.shortcuts import render, HttpResponse, redirect
from users.models import User, Path
from django.http import JsonResponse
# Create your views here.
def signIn(request):
    return render(request, "signIn.html")

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # if User.objects.filter(username=username).exists():
        #     return JsonResponse({'error': 'Username already exists'}, status=400)
        user = User(username=username, password=password, email=email)
        user.save()
        return redirect('signIn')
    return render(request, "signup.html")
    
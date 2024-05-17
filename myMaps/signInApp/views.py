from django.shortcuts import render, HttpResponse, redirect
from users.models import User, Route
from django.http import JsonResponse
from mapsApp.views import maps
# Create your views here.
def signIn(request):
    alert = None
    if request.session.get("alert"):
        alert = request.session.get("alert")
        request.session["alert"] = None
    print(request.session.get("alert"))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username = username)
            if user.password == password:
                request.session["username"] = user.username
                request.session["alert"] = "You have Signed In Successfully"
                return redirect(maps)
        else:
            request.session["alert"] = "That Username Doesnt Exist!"
            return redirect(signUp)
    return render(request, "signIn.html", {"alert": alert})

def signUp(request):
    alert = None
    if request.session.get("alert"):
        print("alert")
        alert = request.session.get("alert")
        request.session["alert"] = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # if User.objects.filter(username=username).exists():
        #     return JsonResponse({'error': 'Username already exists'}, status=400)
        user = User(username=username, password=password, email=email)
        user.save()
        return redirect(signIn)
    return render(request, "signup.html",{"alert":alert})

def signOut(request):
    request.session["username"] = None
    return redirect(signIn)
    
from django.shortcuts import render, HttpResponse, redirect
from users.models import User, Route
from django.http import JsonResponse
from mapsApp.views import maps
# Create your views here.

# render sign in page
def signIn(request):
    # handle alerts
    alert = None
    if request.session.get("alert"):
        alert = request.session.get("alert")
        request.session["alert"] = None
    # if request is post request validate the user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username = username)
            # if password matches redirect to maps
            if user.password == password:
                request.session["username"] = user.username
                request.session["alert"] = "You have Signed In Successfully"
                return redirect(maps)
            else:
                # if password incorrect set an alert and return to sign in
                alert = "Username or Password is doesnt match!!"
                return render(request, "signIn.html", {"alert": alert})
        else:
            # if user doesnt exist redirect to sign up
            request.session["alert"] = "That Username Doesnt Exist!"
            return redirect(signUp)
    return render(request, "signIn.html", {"alert": alert})

def signUp(request):
    # handle alerts
    alert = None
    if request.session.get("alert"):
        print("alert")
        alert = request.session.get("alert")
        request.session["alert"] = None
    # if post request create a new user and redirect to sign In
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

# sign Out of the account
def signOut(request):
    request.session["username"] = None
    return redirect(signIn)
    
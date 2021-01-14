from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.



def presentation(request):
    return render(request, 'presentation.html')


def louboutin(request):
    return render(request, 'louboutin.html')

def chemise(request):
    return render(request, 'chemise.html')
def send(request):
    return render(request, 'send.html')


def talon(request):
    return render(request, 'talon.html')

def all(request):

    return render(request, 'all.html')



def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("inputFirstName")
        lastname = request.POST.get("inputLastName")
        email = request.POST.get("inputEmailAddress")
        username = request.POST.get("inputUsername")
        password = request.POST.get("inputPassword")
        confirmpassword = request.POST.get("inputConfirmPassword")

        if password == confirmpassword:
            user = User(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
            market = Profile(name=firstname)
            if user not in User.objects.filter(username=username, password=password):
                user.save()
                market.save()

        else:

            return redirect('signup')


        return redirect('login')
    return render(request, 'signup.html')



def login(request):
    if request.method == "POST":
        #return  HttpResponse(str(request.method))

        username = request.POST.get("inputUsername")
        password = request.POST.get("inputPassword")

        user = User.objects.filter(username=username, password=password)
        #profil = Profile.objects.filter(username=username, password=password)
        if len(user) > 0:
            request.session["username"] = user[0].username
            return redirect('home.html')

        return render(request, 'login.html')
    print(HttpResponse(str(request.method)))
    return render(request, 'login.html')



def messages(request):
    if request.method == "POST":
        #return  HttpResponse(str(request.method))

        if request.method == "POST":
            name = request.POST.get("inputFirstName")
            message = request.POST.get("inputMessage")
            email = request.POST.get("inputEmailAddress")

        #profil = Profile.objects.filter(username=username, password=password)
        if message == message:
            user = Message(name=name, message=message, email=email)
            messages = Message(name=name)
            if user not in Message.objects.filter(name=name, message=message):
                user.save()
                messages.save()

        else:

            return redirect('home')

        return redirect('send')
    return render(request, 'home.html')


def home(request):
    userform = UsersForm()
    return render(request, 'home.html', {"form": userform})

def maths(request):
    return render(request,'maths.html' )

def logout(request):
    return render(request,'login.html' )





def covid(request):
    return render(request,'covid.html' )


def exo(request):
    return render(request,'exo.html' )

def bac(request):
    return render(request,'bac.html' )

def informatique(request):
    return render(request,'informatique.html' )
def philosophie(request):
    return render(request,'philosophie.html' )
def science(request):
    return render(request,'science.html' )

def chat(request):
    return render(request,'discussion.html' )

def complexe(request):
    return render(request,'complexe.html' )
def fonctions(request):
    return render(request,'fonctions.html' )

def primitives(request):
    return render(request, 'primitives.html')

def integrale(request):
    return render(request, 'integrale.html')

def buy(request):
    if request.method == "POST":
        country = request.POST.get("inputCountry")
        town = request.POST.get("inputTown")
        email = request.POST.get("inputEmailAddress")
        price = request.POST.get("inputPrice")
        password = request.POST.get("inputPassword")
        confirmpassword = request.POST.get("inputConfirmPassword")

        if password == confirmpassword:
            buy = Buy(country=country, town=town, email=email, price=price, password=password)
            market = Buy(name=country)
            if buy not in Buy.objects.filter(country=country, town=town,price=price):
                buy.save()
                market.save()
                return redirect('buy.html')

            else:

                return redirect('sorry.html')

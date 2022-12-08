from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def register(response):
    if response.method == "POST":
        # that will create a new user.
        form = RegisterForm(response.POST)
        if form.is_valid():
            # User created.
            form.save()
        return redirect('/home')
        # redirect will send the user to other page.
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

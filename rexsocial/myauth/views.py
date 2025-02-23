from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
from django.contrib.auth.views import LoginView as DefaultLoginView

from django.contrib.auth.views import LogoutView as DefaultLogoutView

class CustomLogoutView(DefaultLogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Add a success message after logging out
        messages.success(request, "You have successfully logged out!")
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(DefaultLoginView):
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # set staff status to True
            # user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome, " + user.username)
            return redirect("mypost")
        
            # return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "myauth/register.html", {"form": form})
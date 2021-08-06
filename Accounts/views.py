from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
# Create your views here.


# created by Me

def signup(request):
    # save form
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request , user)
            return redirect('/accounts/profile')

    # show form
    else:
        form = SignupForm()
    return render(request , 'registration/signup.html' , {'form' : form})
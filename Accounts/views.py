from django.shortcuts import redirect, render
from .forms import SignupForm ,UserForm,ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
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



def profile(request):
    # get current user
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html', {'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    # save data in form
    if request.method == 'POST':
      userform = UserForm(request.POST,instance=request.user)
      profileform = ProfileForm(request.POST,request.FILES,instance=profile)
      
      # check for the data of form is valid   
      if userform.is_valid() and profileform.is_valid():
          userform.save()
          myprofile = profileform.save(commit=False)
          myprofile.user = request.user
          myprofile.save()
          return redirect(reverse('accounts:profile'))

    # show form
    else:
      userform = UserForm(instance=request.user)
      profileform = ProfileForm(instance=profile)
    
    context = {'userform' :userform , 'profileform' :profileform}
    return render(request, 'accounts/profile_edit.html',context)

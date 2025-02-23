from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

@login_required
def profile_view(request):
    """Display the user's profile"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


@login_required
def profile_update(request):
    """Update the user's profile"""
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/profile_update.html', {'form': form})


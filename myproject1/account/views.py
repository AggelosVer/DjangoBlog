from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, AccountForm ,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def profile(request):
    account = request.user.account
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserRegistrationForm(instance=request.user)
    return render(request, 'account/profile.html', {'user': request.user, 'account': account})

@login_required
def edit_profile(request):
    user = request.user
    account = user.account
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountForm(request.POST, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=user)
        account_form = AccountForm(instance=account)
    return render(request, 'account/edit_profile.html', {'user_form': user_form, 'account_form': account_form})
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

@csrf_exempt
# @csrf_protect
def register(request):
    # return HttpResponse('<p>Hello users</p>')
    if request.method == 'POST':
        print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog:home')
        else:
            messages.error(request, form.errors)
            return redirect('register')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={ 'form': form })


@login_required
def profile(request):

    if request.method == 'POST':
        u_forms = UserUpdateForm(request.POST, instance=request.user)
        p_forms = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_forms.is_valid() and p_forms.is_valid():
            u_forms.save()
            p_forms.save()
            messages.success(request, f'You account has been update!')
            return redirect('users:profile')
        elif u_forms.is_valid():
            messages.error(request, p_forms.errors)
            return redirect('users:profile')
        elif p_forms.is_valid():
            messages.error(request, u_forms.errors)
            return redirect('users:profile')
    else:
        u_forms = UserUpdateForm()
        p_forms = ProfileUpdateForm()

    context = {
        'u_forms': u_forms,
        'p_forms': p_forms
    }
    return render(request, 'users/profile.html', context)
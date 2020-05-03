from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.forms.profile_form import ProfileForm
from user.forms.user_form import UserCreateForm, UserUpdateForm
from user.models import Profile


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


# def update_user(request, id):
#     #TODO: wrong how we are collecting the instance
#     instance = get_object_or_404(User, pk=id)
#     if request.method == 'POST':
#         form = UserUpdateForm(data=request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('game-index')
#             #TODO: redirect to user backend (Edit profile)
#     else:
#         form = UserUpdateForm(instance=instance)
#     return render(request, 'user/update_user.html', {
#         'form': form,
#         'id': id
#     })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })
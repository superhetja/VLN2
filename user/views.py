from django.shortcuts import render, get_object_or_404, redirect
from user.forms.user_form import UserCreateForm, UserUpdateForm
from user.models import User


# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('game-index')
    else:
        form = UserCreateForm()
    return render(request, 'user/create_user.html',  {
        'form': form
    })

def update_user(request, id):
    #TODO: wrong how we are collecting the instance
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('game-index')
            #TODO: redirect to user backend (Edit profile)
    else:
        form = UserUpdateForm(instance=instance)
    return render(request, 'user/update_user.html', {
        'form': form,
        'id': id
    })
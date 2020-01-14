from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm, ChangePasswordForm, SignupForm
from allauth.account.views import LoginView
from django.contrib.auth.models import User
from .models import Profile, Project
from .forms import createForm, editForm, MyCustomLoginForm, MyCustomSetPasswordForm

def home(request):
    title = 'Home'
    return render(request, 'index.html', {'title': title})

def signup(request):
    form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

def login(request):
    form = MyCustomLoginForm()
    return render(request, 'account/login.html', {'form': form})

def resetPassword(request):
    form = MyCustomSetPasswordForm()
    return render(request, 'account/login.html', {'form': form})


def changePassword(request):
    form = ChangePasswordForm()
    return render(request, 'registration/changepassword.html', {'form': form})

def profile(request, user_id):
    user = request.user
    posts = Project.objects.filter(profile_id = user_id)
    for post in posts:
        name = post.image_name.split()
        if len(name) > 1:
            post.image_name = '_'.join(name)
        else:
            pass
    # username = user.get_username
    username = user.get_username()
    form = editForm()
    create_form = createForm()
    # if request.method == "POST":
    #     form = editForm(request.POST, request.FILES)
    #     create_form = createForm(request.POST, request.FILES)
    #     if form.is_valid() and create_form.is_valid():
    #         image = create_form.save(commit = False)
    #         profile = form.save(commit=False)
    #         profile.user = request.user
    #         image.profile_user = request.user
    #         profile.save()
    #         image.save()
            
    # else:
    #     form = editForm()
    #     create_form = createForm()

    try:
        u = User.objects.get(id = user_id)
        profile = u.profile
        username = u.username
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'form': form, 'posts': posts, 'create_form': create_form, 'profile': profile, 'username': username, 'user': user})


def create_post(request):
    form = createForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit = False)
        post.profile = request.user
        post.save()
        print("post has been created")
    return redirect('profile', user_id = request.user.id)


def update_profile(request):
    if request.method == 'POST':
        
        form = editForm(request.POST, request.FILES)
        if form.is_valid():
            usr = request.user
            Profile.objects.filter(user_id=usr.id).delete()
            # photo = request.POST['photo']
            # bio = request.POST['bio']
            # profile = Profile.objects.filter(user_id = request.user.id).update(photo = photo, bio = bio)
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
        return redirect('profile', user_id = request.user.id)
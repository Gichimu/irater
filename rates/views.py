from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm, ChangePasswordForm, SignupForm
from allauth.account.views import LoginView
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
from .forms import createForm, editForm, MyCustomLoginForm, MyCustomSetPasswordForm, ratingForm

def home(request):
    title = 'Home'
    try:
        posts = Project.objects.all()
        for post in posts:
            name = post.title.split()
            if len(name) > 1:
                post.title = '_'.join(name)
            else:
                pass
    except Project.DoesNotExist:
        posts = None
    return render(request, 'index.html', {'title': title, 'posts': posts})

def signup(request):
    form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

# def login(request):
#     form = MyCustomLoginForm()
#     return render(request, 'account/login.html', {'form': form})

def resetPassword(request):
    form = MyCustomSetPasswordForm()
    return render(request, 'account/login.html', {'form': form})


def changePassword(request):
    form = ChangePasswordForm()
    return render(request, 'registration/changepassword.html', {'form': form})

def profile(request, user_id):
    user = request.user
    try:
        prof = Profile.objects.get(user_id = user_id)
        posts = Project.objects.filter(profile_id = prof.id)
        for post in posts:
            name = post.title.split()
            if len(name) > 1:
                post.title = '_'.join(name)
            else:
                pass
    except Profile.DoesNotExist:
        posts = None
    
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
    # profile = Profile.objects.filter(user_id = request.user.id)
    if form.is_valid():
        # title = request.POST.get['title']
        # desc = request.POST['description']
        # photo = request.POST['photo']
        # url = request.POST['link']
        # print(title)
        # post = Project(title = title, description = desc, photo = photo, link = url)
        post = form.save(commit = False)
        post.profile = request.user
        post.save()
        print("post has been created")
    return redirect('profile', user_id = request.user.id)


def update_profile(request):
    form = editForm(request.POST, request.FILES)
    if form.is_valid():
        usr = request.user
        try:
            prof = Profile.objects.filter(user_id=usr.id)
            prof.delete()
            # photo = request.POST['photo']
            # bio = request.POST['bio']
            # profile = Profile.objects.filter(user_id = request.user.id).update(photo = photo, bio = bio)
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
        except Profile.DoesNotExist:
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
    return redirect('profile', user_id = request.user.id)


def post(request, post_id):
    post = Project.objects.get(pk = post_id)
    form = ratingForm()
    # if request == 'POST':
    #     form = ratingForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         usability = request.POST.get('usability')
    #         design = request.POST.get('design')
    #         content = request.POST.get('content')

    #         average = (usability + design + content) / 3
    #         post = form.save(commit = False)
    #         post.avg = average
    #         post.save()
    #         print('your rating has been sent')
    # else:
    #     form = ratingForm()
    return render(request, 'post.html', {'post': post, 'form': form})

def rate(request, post_id):
    form = ratingForm(request.POST, request.FILES)
    try:
        rating = Rating.objects.get(post = post_id)
    except Rating.DoesNotExist:
        rating = None

    if form.is_valid():
        usability = request.POST.get('usability')
        design = request.POST.get('design')
        content = request.POST.get('content')

        avg = (int(usability) + int(design) + int(content)) / 3
        if rating:
            average = (avg + rating.avg) / 2
        else:
            average = avg 
        rate = form.save(commit = False)
        rate.avg = average
        # rate.post = post_id
        rate.save()
        print('your rating has been sent')
    return redirect('post', post_id = post_id)
    

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AuthorProfile, Article, Book
from .forms import ArticleForm, BookForm
from .forms import AuthorProfileForm
from django.contrib.auth.models import User
from django.contrib import messages


def author_welcome(request):
    return render(request, 'author/welcome.html')


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'author/create_article.html', {'form': form})

@login_required
def publish_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'author/publish_book.html', {'form': form})

@login_required
def author_profile_setup(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        bio = request.POST.get('bio')
        expertise = request.POST.get('expertise')
        achievements = request.POST.get('achievements')

        AuthorProfile.objects.create(
            user=request.user,
            profile_image=profile_image,
            bio=bio,
            expertise=expertise,
            achievements=achievements,
        )
        return redirect('author_profile_setup')

    return render(request, 'author/profile_setup.html')


def create_author_profile(request):
    if request.method == 'POST':
        # process form data...
        # save author profile...
        messages.success(request, "Your profile was created successfully!")
        return redirect('author_dashboard')  # 👈 Redirect after success

    return render(request, 'author/create_author_profile.html')

def author_dashboard(request):
    return render(request, 'author/author_dashboard.html')  # Create this template
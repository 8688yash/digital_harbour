from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post, Message, Skill, Certificate
from .forms import RegistrationForm, UserProfileForm, PostForm, MessageForm, CertificateForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post
from .forms import PostForm


def community_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community/home.html', {'posts': posts})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # auto-create profile
            login(request, user)
            return redirect('community_home')
    else:
        form = RegistrationForm()
    return render(request, 'community/register.html', {'form': form})

@login_required
def profile_view(request, user_id=None):
    user = request.user if not user_id else get_object_or_404(User, pk=user_id)
    profile = UserProfile.objects.get(user=user)
    return render(request, 'community/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        cert_form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        if cert_form.is_valid():
            cert = cert_form.save(commit=False)
            cert.user = request.user
            cert.save()
            profile.certificates.add(cert)
        return redirect('profile', user_id=request.user.id)
    else:
        form = UserProfileForm(instance=profile)
        cert_form = CertificateForm()
    return render(request, 'community/edit_profile.html', {'form': form, 'cert_form': cert_form})

@login_required
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community_home')
    else:
        form = PostForm()
    return render(request, 'community/post.html', {'form': form})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'community/message.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'community/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'community/sent.html', {'messages': messages})

def search_users(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = UserProfile.objects.filter(
            Q(user__username__icontains=query) |
            Q(bio__icontains=query) |
            Q(skills__name__icontains=query)
        ).distinct()
    return render(request, 'community/search_results.html', {'results': results})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community_home')
    else:
        form = PostForm()
    return render(request, 'community/create_post.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('community_home')  # Adjust this to your community home view name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'community/login.html')


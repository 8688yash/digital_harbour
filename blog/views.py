from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.db.models import Q

from .models import Blog, LibraryItem, AuthorProfile, Subscribe, Freebie, MarketplaceItem, CommunityPost, GalleryImage, Category
from .forms import blogForm, LibraryItemForm, AuthorRegistrationForm
from author.models import Book
from whitepapers.models import Whitepaper


# BASIC PAGES
def home(request):
    blogs = Blog.objects.filter(published=True).order_by('-created_at')[:3]
    return render(request, 'blog/home.html', {'blogs': blogs})

def about(request): return render(request, 'blog/about.html')
def contact(request): return render(request, 'blog/contact.html')
def privacy(request): return render(request, 'blog/privacy_policy.html')
def terms(request): return render(request, 'blog/terms.html')
def mission(request): return render(request, 'blog/mission.html')
def vision(request): return render(request, 'blog/vision.html')
def who_we_are(request): return render(request, 'blog/who_we_are.html')
def freebies(request): return render(request, 'blog/freebies.html')
def marketplace(request): return render(request, 'blog/marketplace.html')
def community(request): return render(request, 'community/community_home.html')


# BLOG
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    domains = ['Technology', 'Design', 'Education', 'Startups', 'AI & ML', 'Marketing']
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'domains': domains})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def search_blogs(request):
    query = request.GET.get('q', '')
    blogs = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(tags__name__icontains=query) |
        Q(pdf_text__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'blogs': blogs, 'query': query})


# LIBRARY
from .models import LibraryPDF  # Assuming model name

def library(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    library_pdfs = LibraryPDF.objects.all()

    if query:
        library_pdfs = library_pdfs.filter(title__icontains=query)

    if category:
        library_pdfs = library_pdfs.filter(category__iexact=category)

    context = {
        'library_pdfs': library_pdfs,
        'books': Book.objects.all(),  # If needed
        # 'blogs': Blog.objects.all(),  # You can remove this if not required
    }
    return render(request, 'blog/library.html', context)

def library_view(request):
    return render(request, 'blog/library.html') 


# SUBSCRIPTION
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and not Subscribe.objects.filter(email=email).exists():
            Subscribe.objects.create(email=email)
            messages.success(request, "Subscribed successfully!")
        else:
            messages.warning(request, "You are already subscribed.")
        return redirect('home')
    return HttpResponse('Invalid Request', status=400)

def subscribe_view(request):
    features = [
        ('Growth Tactics', 'Monetize through SEO, email funnels, and branding.', 'growth.png'),
        ('Startup Ideas', 'Lean MVPs, emerging tech, and trend analysis.', 'startup.png'),
        ('Freebies Monthly', 'Templates, assets, toolkits — completely free.', 'freebies.png'),
        ('Remote Work', 'Curated global job links and digital internships.', 'remote.png'),
    ]
    return render(request, 'blog/subscribe.html', {'features': features})


# AUTHOR
@login_required
def author_dashboard(request):
    blogs = Blog.objects.filter(author=request.user)
    library_items = LibraryItem.objects.filter(uploaded_by=request.user)
    return render(request, 'blog/author_dashboard.html', {
        'blogs': blogs, 'library_items': library_items
    })


# GALLERY
def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})


# PDF VIEW
def view_pdf(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return FileResponse(blog.pdf_file.open(), content_type='application/pdf')

def view_pdf_by_id(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return FileResponse(blog.pdf_file.open(), content_type='application/pdf')


# WHITEPAPER
def whitepaper_home(request):
    return render(request, 'whitepapers/whitepaper_home.html')

def whitepaper_list(request, category):
    whitepapers = Whitepaper.objects.filter(category__name=category)
    return render(request, 'whitepapers/whitepaper_list.html', {'whitepapers': whitepapers, 'category': category})

def whitepaper_detail(request, pk):
    whitepaper = get_object_or_404(Whitepaper, pk=pk)
    return render(request, 'whitepapers/whitepaper_detail.html', {'whitepaper': whitepaper})

def submit_whitepaper(request):
    if request.method == 'POST':
        # Example: Whitepaper.objects.create(title=..., description=...)
        return HttpResponse('Whitepaper submitted successfully!')
    return render(request, 'whitepapers/submit_whitepaper.html')

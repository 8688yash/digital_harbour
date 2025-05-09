from django.shortcuts import render, redirect, get_object_or_404
from .models import Whitepaper
from .forms import WhitepaperForm
from django.contrib.auth.decorators import login_required

def whitepaper_home(request):
    categories = set([cat[0] for cat in Whitepaper._meta.get_field('category').choices])
    return render(request, 'whitepapers/home.html', {'categories': categories})

def whitepaper_list(request, category=None):
    whitepapers = Whitepaper.objects.filter(published=True)
    if category:
        whitepapers = whitepapers.filter(category=category)
    return render(request, 'whitepapers/list.html', {'whitepapers': whitepapers, 'category': category})

def whitepaper_detail(request, pk):
    whitepaper = get_object_or_404(Whitepaper, pk=pk, published=True)
    return render(request, 'whitepapers/detail.html', {'whitepaper': whitepaper})

@login_required
def submit_whitepaper(request):
    if request.method == 'POST':
        form = WhitepaperForm(request.POST, request.FILES)
        if form.is_valid():
            wp = form.save(commit=False)
            wp.author = request.user
            wp.save()
            return redirect('whitepaper_home')
    else:
        form = WhitepaperForm()
    return render(request, 'whitepapers/submit.html', {'form': form})

def view_whitepaper(request, pk):
    whitepaper = get_object_or_404(Whitepaper, pk=pk)
    return render(request, 'whitepapers/view_whitepaper.html', {'whitepaper': whitepaper})

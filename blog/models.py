from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from pdfminer.high_level import extract_text


# TAG SYSTEM
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# CATEGORY SYSTEM
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

def get_default_category():
    category, created = Category.objects.get_or_create(name='Uncategorized')
    return category.id

# BLOG SYSTEM
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='blog_pdfs/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    pdf_text = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.pdf_file:
            try:
                self.pdf_text = extract_text(self.pdf_file)
            except Exception as e:
                self.pdf_text = f"Error extracting text: {e}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# LIBRARY SYSTEM
CATEGORY_CHOICES = [
    ('whitepaper', 'Whitepaper'),
    ('ebook', 'eBook'),
    ('manual', 'Manual'),
    ('research', 'Research'),
    ('guide', 'Guide'),
    ('other', 'Other'),
]
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LibraryItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    cover_image = models.ImageField(upload_to='library/covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='library_pdfs/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Library Item'
        verbose_name_plural = 'Library Items'

    def __str__(self):
        return self.title


class LibraryPDF(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='library_pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# FREEBIES SYSTEM
class Freebie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='freebies/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# MARKETPLACE SYSTEM
class MarketplaceItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    file = models.FileField(upload_to='marketplace/')
    cover_image = models.ImageField(upload_to='marketplace/images/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# COMMUNITY SYSTEM
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

# AUTHOR PROFILE
class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog_author_profile')
    bio = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# SUBSCRIPTION
class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# GALLERY SYSTEM
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# BOOK MODEL
class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

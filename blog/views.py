from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='P').order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def home(request):
    posts = Post.objects.filter(status='P').order_by('-created_at')[:4]  # Latest 4 published posts
    return render(request, 'home.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

from .models import Post

def blog_home(request):
    posts = Post.objects.filter(status='P').order_by('-created_at')
    return render(request, 'blog/blog_home.html', {'posts': posts})

def contact_submit(request):
    if request.method == 'POST':
        print("🚀 Contact form received a POST request")  # Add this
        form = ContactForm(request.POST)
        if form.is_valid():
            print("✅ Contact form is valid, preparing to send email")  # Add this
            send_mail(
                subject=f"Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['test@example.com'],
            )
            return redirect('home')
    print("❌ Contact form submission failed or was GET")
    return redirect('home')


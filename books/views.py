from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.status = 'pending'  # Set status to pending
            book.save()
            return redirect('pending_books')  # Redirect to a page showing pending books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    # books = Book.objects.all()
    books = Book.objects.filter(status='approved')  # Only approved books
    return render(request, 'book_list.html', {'books': books})

def signup_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Account created successfully!")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match!")
    
    return render(request, "signup_page.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "login_page.html")

def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

def home(request):
    return render(request, "home.html")  # Placeholder for book listing

@login_required(login_url='/login/')  # Redirect to login page if not logged in
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.status = 'pending'  # Set status to pending
            book.save()
            messages.success(request, 'Book added successfully! Waiting for admin approval.')
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def pending_books(request):
    """ Show books submitted by users but not yet approved """
    pending_books = Book.objects.filter(status='pending')
    return render(request, 'pending_books.html', {'pending_books': pending_books})
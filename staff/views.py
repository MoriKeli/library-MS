from datetime import datetime
from staff.forms import AddNewBookForm, LoginForm, RateBooksReturned, SignUpForm, UpdateProfileForm, EditProfileForm, BorrowBooksForm, BookReturnedForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from staff.models import Librarian, Book, Student
from .utils import get_plot
import numpy as np


class LibrarianLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'staff/login.html'
    
    
def signup_view(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            lib = form.save(commit=False)
            lib.username = lib.first_name + ' ' + lib.last_name
            lib.is_staff = True
            lib.save()
            
            messages.success(request, 'You have successfully created an account')
            return redirect('profile')
    
    context = {'form': form}
    return render(request, 'staff/signup.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff)
def profile_view(request):
    updateprofile = UpdateProfileForm(instance=request.user.librarian)
    edit_profile = EditProfileForm(instance=request.user.librarian)
    
    if request.method == 'POST':
        updateprofile = UpdateProfileForm(request.POST, request.FILES, instance=request.user.librarian)
        edit_profile = EditProfileForm(request.POST, request.FILES, instance=request.user.librarian)
        
        if updateprofile.is_valid():
            updateprofile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('homepage')
        
        elif edit_profile.is_valid():
            edit_profile.save()
            
            messages.info(request, 'Profile edited successfully!')
            return redirect('profile')
        
    context = {'update_form': updateprofile, 'edit_form': edit_profile}
    return render(request, 'staff/profile.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff)
def homepage_view(request):
    borrow_form = BorrowBooksForm()
    newbook_form = AddNewBookForm()
    
    if request.method == 'POST':
        borrow_form = BorrowBooksForm(request.POST)
        newbook_form = AddNewBookForm(request.POST, request.FILES)

        if borrow_form.is_valid():
            book = borrow_form.save(commit=False)
            
            filter_book = Book.objects.filter(ref_no=book.ref_no, title=book.title, author=book.author).exists()
            if filter_book is True:
                if Student.objects.filter(ref_no=book.ref_no, returned=False).exists():
                    messages.error(request, 'This book is already borrowed! Check you have entered the correct Reference No.!')
                else:
                    book.total_books += 1
                    book.save()
            
                    messages.info(request, f'Book: {book.title} has been borrowed by {book.name}.')
                    return redirect('homepage')

            else:
                messages.error(request, 'Book details provided may be incorrect.')
            
        elif newbook_form.is_valid():
            newBook = newbook_form.save(commit=False)
            
            book_info = Book.objects.filter(catalogue=newBook.catalogue).exists()
            if book_info is True:
                messages.error(request, 'This catalogue no. already exists!')
            
            else:
                newBook.save()
                messages.success(request, f'Book "{newBook.title}" has been added successfully!')
                return redirect('books')
    
    
    total_books = Book.objects.all().count()
    total_staff = Librarian.objects.all().count()
    past_dueDate = Student.objects.filter().count()
    male_bookwormers = Student.objects.filter(gender='Male').count()
    female_bookwormers = Student.objects.filter(gender='Female').count()
    bookwormers = Student.objects.filter(total_books__gt=0).first()
    borrowed_books = Student.objects.filter(returned=False).all()
    m = Student.objects.filter(borrowed__date__contains=datetime.now().strftime("%Y-%m"), returned=False)
    chart = get_plot('val', borrowed_books.count())

    context = {
        'borrow_book': borrow_form, 'add_new_book': newbook_form, 'total_books': total_books, 'staff': total_staff,
        'BooksPastDueDate': past_dueDate, 'maleReaders': male_bookwormers, 'femaleReaders': female_bookwormers,
        'bookwormers': bookwormers, 'total_borrowed_books': borrowed_books.count(), 'borrowed_books': borrowed_books.order_by('-borrowed'),
        'books_returned': Student.objects.filter(returned=True).count(),
        'chart': chart,
        }
    return render(request, 'staff/homepage.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff)
def bookslist_view(request):
    books_lib = Book.objects.all().order_by('title')
    borrowed_books = Student.objects.filter(returned=False)
    editform = AddNewBookForm()
    
    if request.method == 'POST':
        editform = AddNewBookForm(request.POST,)
    
    context = {
        'books_in_the_library': books_lib, 'total_books': books_lib.count(), 'borrowed': borrowed_books.count(),
        'editform': editform,
        }
    return render(request, 'staff/books.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff)
def returnbooks_view(request, pk):
    obj = Student.objects.get(ref_no=pk, returned=False)
    book_info = Book.objects.get(ref_no=obj.ref_no)
    print(f'Book info.: {book_info}')
    return_form = BookReturnedForm(instance=obj)
    bookrating_form = RateBooksReturned(instance=book_info)
    
    if request.method == 'POST':
        return_form = BookReturnedForm(request.POST, instance=obj)
        bookrating_form = RateBooksReturned(request.POST, instance=book_info)
        
        if return_form.is_valid():
            form = return_form.save(commit=False)
            form.returned = True
            form.save()
           
            if bookrating_form.is_valid():
                bookrating_form.save()
                
            messages.success(request, f'Book {form.title} has been returned.')
            return redirect('books')
        

    context = {'return_book': return_form, 'book_info': book_info, 'obj': obj, 'rate_form': bookrating_form}
    return render(request, 'staff/return-form.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff)
def edit_view(request, ref):
    obj = Book.objects.get(ref_no=ref)
    editform = AddNewBookForm(request.POST or None, instance=obj)
    
    if editform.is_valid():
        editform.save()
        messages.warning(request, f'You have updated details for book "{obj.title}"')
        return redirect('edit-delete', ref)
    
    if request.method == 'POST':
        obj.delete()
        messages.error(request, f'You have deleted "Book: {obj.title} - ref.no.{obj}"')
        return redirect('books')
        
    context = {'obj': obj, 'editform': editform}
    return render(request, 'staff/edit.html', context)


class LogoutLibrarian(LogoutView):
    template_name = 'staff/logout.html'
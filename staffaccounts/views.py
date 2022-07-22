from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from staffaccounts.models import *

# Python modules
from datetime import datetime

def login(request):
    if request.method == 'POST':
        staffname = request.POST['staffname']
        staff_password = request.POST['password']

        staff = auth.authenticate(username=staffname, password=staff_password)

        if staff is not None:
            auth.login(request, staff)
            return redirect(f'homepage/{staff.pk}')
        else:            
            if staff_password != auth.authenticate(paswword=staff_password) and User.objects.filter(username=staffname).exists():
                messages.warning(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'Invalid Credentials. Please try again.')
            return redirect('/')

    return render(request, 'staff/staff_login.html')

def register(request):
    if request.method == 'POST':
        staff_name = request.POST['staffname']
        gender = request.POST['gender']
        phone = request.POST['phone_no']
        staff_email_addr = request.POST['email']
        role = request.POST['role']
        password1 = request.POST['password']
        password2 = request.POST['re-enter-password']

        if len(staff_name) > 50:
            messages.warning(request, 'Staff name provided is too long')
        elif len(password1) < 8 or len(password2) < 8:
            messages.error(request, 'Password(s) too short. Your password(s) should have atleast 8 characters.')
        elif password1 != password2:
            messages.error(request, 'Passowrd(s) not matching!')
        else:
            staff = True
            if staff is True:
                save_staff = User.objects.create_user(username=staff_name, email=staff_email_addr, password=password2, is_staff=True)
                save_staff.save()
                staff_details = Librarian.objects.create(name=staff_name, gender=gender, lib_mobile_no=phone, role=role)
                staff_details.save()

                messages.success(request, f'Staff "{staff_name}" registered successfully.')
                return redirect('/')

    return render(request, 'staff/staff_register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='staff_login')
def homepage(request, pk):
    lib_id = User.objects.get(id=pk)

    # profile of each librarian
    gender = Librarian.objects.filter(gender="male").order_by('gender')
    role = Librarian.objects.filter(role="librarian")

    # total no. of borrowed books = no. of borrowed books - no. of returned books
    no_books_borrowed = (Student.objects.filter(status="borrow").count()) - (Student.objects.filter(status="return").count())

    # total no. of books in the library:
    total_no_of_books = (Books.objects.all().count()) - no_books_borrowed
    
    # students who have borrowed books.
    books_borrowed = Student.objects.filter(status="borrow")

    context = {'id': lib_id, 'gender': gender, 'roles': role, 'books_borrowed': no_books_borrowed,
     'list_of_borrowed_books': books_borrowed, 'total': total_no_of_books,}

    return render(request, 'staff/homepage.html', context)

@login_required(login_url='staff_login')
def borrow_book(request):
    if request.method == 'POST':
        student_name = request.POST['studentname']
        gender = request.POST['gender']
        phone_no = request.POST['phone_no']
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        yop = request.POST['year-of-publication']
        ref_no = request.POST['ref_no']
        book_type = request.POST['type-of-book']
        state = request.POST['status']

        if (state == 'borrow') and (Student.objects.filter(book_ref_no=ref_no).exists()):
            messages.error(request, f'Book with ref.no "{ref_no}" has been borrowed.')
        elif state == 'return':
            date_returned = request.POST['d-returned']

            returned = Student.objects.create(stud_name=student_name, gender=gender, stud_mobile_no=phone_no, title=title, type_of_book=book_type,
             author=author, publisher=publisher, year_of_publication=yop, book_ref_no=ref_no, date_returned=date_returned, status=state,)
            returned.save()
            messages.success(request, f"{student_name} returned {title} today.")

        else:
            save_record = Student.objects.create(stud_name=student_name, gender=gender, stud_mobile_no=phone_no,
                title=title, author=author, publisher=publisher, year_of_publication=yop, book_ref_no=ref_no, type_of_book=book_type, status=state,
            )
            save_record.save()
            messages.success(request, f"{student_name} borrowed {title} today.")
    
    return render(request, 'staff/borrow-book.html')

@login_required(login_url='staff_login')
def add_book_record(request):
    if request.method == 'POST':
        book_title = request.POST['title']
        book_author = request.POST['author']
        book_publisher = request.POST['publisher']
        book_yop = request.POST['year']
        type_of_book = request.POST['type-of-book']
        book_ref_no = request.POST['ref_no']

        if (Books.objects.filter(book_ref_no=book_ref_no).exists()):
            messages.error(request, 'Book record already exists')
        else:
            add_record = Books.objects.create(book_ref_no=book_ref_no, title=str(book_title).title(), author=str(book_author).title(), publisher=str(book_publisher).title(), year_of_publication=book_yop, type_of_book=type_of_book)
            add_record.save()

            messages.success(request, f'Record for "{book_title}" added succesfully')

    return render(request, 'staff/add-book.html')

@login_required(login_url='staff_login')
def search_for_a_book(request):
    books = Books.objects.all()
    context = {}
    if request.method == 'POST':
        search = request.POST['search-book']
        search = search.title()
        
        if (Books.objects.filter(title=search).exists()):
            messages.info(request, 'Book record found')

            # book info to be displayed on the template
            book_title = Books.objects.filter(title=search)
            
            context = {'title': book_title}
            
        else:
            messages.error(request, f'Book record searched by criteria "{search}" not found.')

    return render(request, 'staff/search-form.html', context)


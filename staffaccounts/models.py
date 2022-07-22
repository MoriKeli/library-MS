from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Librarian(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, unique=True)
    lib = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=6, blank=False, null=False)
    lib_mobile_no = models.CharField(max_length=10, null=False, blank=False)
    role = models.CharField(max_length=20, null=False, blank=False)
    profile_pic = models.ImageField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Account for {self.name} created on {self.created.strftime("%a %dth-%m-%Y %H:%M:%S")}'
        # return f'{self.gender}'

# database containing all books in the lib.
class Books(models.Model):
    book_ref_no = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    publisher = models.CharField(max_length=150, null=False, blank=False)
    year_of_publication = models.CharField(max_length=4, null=False, blank=False)
    type_of_book = models.CharField(max_length=50, null=False, blank=False)
    book_photo = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book "{self.title}" was added on {self.created.strftime("%A %dth-%m-%Y")} at {self.created.strftime("%H:%M:%S")}'

    class Meta:
        verbose_name_plural = 'Books'

# db of the borrowers
class Student(models.Model):    
    stud_id = models.UUIDField(default=uuid.uuid4(), editable=False)
    stud_name = models.CharField(max_length=150, null=False, blank=False)
    stud_mobile_no = models.CharField(max_length=10, null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False)
    
    # book details
    book_ref_no = models.CharField(max_length=30, null=True, blank=False)
    title = models.CharField(max_length=100, null=True, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)
    publisher = models.CharField(max_length=150, null=False, blank=False)
    year_of_publication = models.CharField(max_length=4, null=False, blank=False)
    type_of_book = models.CharField(max_length=50, null=False, blank=False)
    book_photo = models.ImageField()
    status = models.CharField(max_length=10, null=False, blank=False)
    fine = models.FloatField(null=True, default=0, blank=True)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        if self.status == 'borrow':
            return f"{self.stud_name} borrowed \"{self.title}\" on {self.date_borrowed.strftime('%A %dth-%m-%Y %H:%M:%S')}"

        return f"{self.stud_name} returned \"{self.title}\" on {self.date_borrowed.strftime('%A %dth-%m-%Y %H:%M:%S')}"

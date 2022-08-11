from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Librarian(models.Model):
    id = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    lib = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    dp = models.ImageField(upload_to='Dps/', default='default.png')
    gender = models.CharField(max_length=10, blank=False)
    mobile_no = models.CharField(max_length=14, blank=False)
    library = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=10, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.lib.username}'
    
    def save(self, *args, **kwargs):
        super(Librarian, self).save(*args, **kwargs)
        
        pic = Image.open(self.dp.path)
        
        if pic.height > 500 and pic.width > 500:
            output_size = (500, 500)
            pic.thumbnail(output_size)
            pic.save(self.pic.path)
    
    class Meta:
        ordering = ['lib']
    

class Book(models.Model):
    ref_no = models.CharField(max_length=12, primary_key=True, unique=True, editable=False)
    catalogue = models.CharField(max_length=20, blank=False)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    published = models.CharField(max_length=4, blank=False)
    publisher = models.CharField(max_length=50, blank=False)
    type = models.CharField(max_length=60, blank=False)
    image = models.ImageField(upload_to='Books/', default='icon.png')
    rating = models.CharField(max_length=3, blank=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class Student(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, blank=False)
    phone_no = models.CharField(max_length=10, blank=False)
    residence = models.CharField(max_length=50, blank=False)
    school = models.CharField(max_length=50, blank=False)
    ref_no = models.CharField(max_length=15, blank=False)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=150, blank=False)
    returned = models.BooleanField(default=False, blank=False, editable=False)
    total_books = models.PositiveIntegerField(default=0, editable=False)
    fine = models.PositiveIntegerField(default=0, editable=False)
    borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']

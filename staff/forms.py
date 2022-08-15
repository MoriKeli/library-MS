from staff.models import Librarian, Book, Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        
        self.fields['username'].label = 'Enter your name'
        self.error_messages['invalid_login'] = 'Invalid credentials! Please enter the name you used to create an account. Username & password may be case-sensitive'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        

class UpdateProfileForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CHOICE_ROLE = (
        (None, '-- Select your role --'),
        ('Librarian', 'Librarian'),
        ('Assistant Librarian', 'Assistant Librarian'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=CHOICE_GENDER)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Enter your mobile no.', 'class': 'mb-2'}), label='')
    library = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your library', 'class': 'mb-2'}), label='')
    role = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_ROLE, label='')
    location = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the location of your library', 'class': 'mb-2'}), label='')
    dp = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mb-2'}), help_text='Attach your image', required=True, label='')
    
    class Meta:
        model = Librarian
        fields = ['gender', 'mobile_no', 'library', 'role', 'location', 'dp']


class EditProfileForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CHOICE_ROLE = (
        (None, '-- Select your role --'),
        ('Librarian', 'Librarian'),
        ('Assistant Librarian', 'Assistant Librarian'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=CHOICE_GENDER, disabled=True)
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Enter your mobile no.', 'class': 'mb-2'}), label='', disabled=True)
    library = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the name of your library', 'class': 'mb-2'}), label='', disabled=True)
    role = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=CHOICE_ROLE, disabled=True, label='')
    location = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter the location of your library', 'class': 'mb-2'}), label='', disabled=True)
    dp = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'mb-2'}), help_text='Attach your image', required=True, label='')
    
    class Meta:
        model = Librarian
        fields = ['gender', 'mobile_no', 'library', 'role', 'location', 'dp']


class AddNewBookForm(forms.ModelForm):
    CHOICE_TYPE = (
        (None, '-- Select type of this book --'),
        ('Biography', 'Biography'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Encyclopedia', 'Encyclopedia'),
        ('Geography', 'Geography'),
        ('History', 'History'),
        ('Inspirational', 'Inspirational'),
        ('Mathematics', 'Mathematics'),
        ('Novel', 'Novel'),
        ('Physics', 'Physics'),
        ('Science', 'Science'),
        ('Religion', 'Religion'),
        ('Textbook', 'Textbook'),
    )
    published = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'maxlength': '4'}))
    type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), label='Type of book', choices=CHOICE_TYPE)
    class Meta:
        model = Book
        exclude = ['rating']

class BorrowBooksForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select the gender of the student --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CHOICE_TYPE = (
        (None, '-- Select type of this book --'),
        ('Biography', 'Biography'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Encyclopedia', 'Encyclopedia'),
        ('Geography', 'Geography'),
        ('History', 'History'),
        ('Inspirational', 'Inspirational'),
        ('Mathematics', 'Mathematics'),
        ('Novel', 'Novel'),
        ('Physics', 'Physics'),
        ('Science', 'Science'),
        ('Religion', 'Religion'),
        ('Textbook', 'Textbook'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter the name of the student ...'}), label='')
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=CHOICE_GENDER)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2', 'placeholder': 'Enter mobile no. of this student ...'}), label='')
    residence = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter the residence of the student ...'}), label='')
    school = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter school of the student ...'}), label='')
    ref_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter Ref. No. of the book borrowed ...'}), label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter the title of the book ...'}), label='')
    author = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter author of the book ...'}), label='')
    type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='Type of Book', choices=CHOICE_TYPE)
    
    class Meta:
        model = Student
        fields = ['name', 'gender', 'phone_no', 'residence', 'school', 'ref_no', 'title', 'author', 'type']
        
class BookReturnedForm(forms.ModelForm):
    CHOICE_GENDER = (
        (None, '-- Select the gender of the student --'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', choices=CHOICE_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), label='', disabled=True)
    residence = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)
    school = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)
    ref_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)
    author = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), label='', disabled=True)

    class Meta:
        model = Student
        fields = ['name', 'gender', 'phone_no', 'residence', 'school', 'ref_no', 'title', 'author',]
        
class RateBooksReturned(forms.ModelForm):
    CHOICE_RATE = (
        (None, '-- Select one option --'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    
    rating = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), label='', 
        help_text='How does the student rate this book on a scale of 5?', choices=CHOICE_RATE
        )
    
    class Meta:
        model = Book
        fields = ['rating']
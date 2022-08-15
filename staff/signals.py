import uuid
from staff.models import Librarian, Book, Student
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from uuid import uuid4


@receiver(pre_save, sender=Librarian)
def generate_librarian_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid4()).upper().replace("-", "")[:10]


@receiver(pre_save, sender=Book)
def generate_book_id(sender, instance, **kwargs):
    if instance.ref_no == "":
        instance.ref_no =str(uuid4()).upper().replace("-", "")[:15]

@receiver(pre_save, sender=Student)
def generate_student_id(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid4()).replace("-", "").upper()[:15]

@receiver(post_save, sender=User)
def librarian_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is True and instance.is_superuser is False:
            Librarian.objects.create(lib=instance)
# Generated by Django 4.0.3 on 2022-05-14 07:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('staffaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb818175-59de-4628-8735-e68b225b0e2e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_id',
            field=models.UUIDField(default=uuid.UUID('b7422639-a2dc-409f-a3ce-59ea4c50f9da'), editable=False),
        ),
    ]
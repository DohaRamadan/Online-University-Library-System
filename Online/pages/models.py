from django.db import models
from django.db import models
from django.db.models.fields import AutoField
from django.utils.translation import ugettext_lazy as _
from django.db.models.enums import Choices
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


# Create your models here.

class Book(models.Model):
    book_status = [
        ('Available', 'Available'),
        ('Borrowed', 'Borrowed'),
    ]
    id = AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    borrowing_period = models.IntegerField(null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    isbn = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=book_status, null=True, blank=True)
    slug = models.SlugField(_("slug"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


# Create your models here.
class Bookdetails:
    book_status = [
        ('Available', 'available'),
        ('Borrowed', 'Borrowed'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    borrowing_period = models.IntegerField(null=True, blank=True)
    isbn = models.IntegerField(null=True, blank=True, unique=True)
    status = models.CharField(max_length=50, choices=book_status, null=True, blank=True)
    slug = models.SlugField(_("slug"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

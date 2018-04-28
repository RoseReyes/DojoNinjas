from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<name: {}, desc: {}, created_at: {}, updated_at: {}>".format(self.name, self.desc, self.created_at, self.updated_at)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    desc = models.TextField(default="")
    # a book can have many authors and an author can have many books
    books = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<id: {}, first_name: {}, last_name: {}, email: {}, created_at: {}, updated_at: {}>".format(self.id, self.first_name, self.last_name, self.email, self.created_at, self.updated_at)
        
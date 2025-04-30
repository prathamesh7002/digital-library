from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    subject_filter = request.GET.get('subject')

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    if subject_filter:
        books = books.filter(subject=subject_filter)

    subjects = Book.SUBJECT_CHOICES
    return render(request, 'library/book_list.html', {'books': books, 'subjects': subjects})
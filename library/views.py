from django.shortcuts import render, get_object_or_404
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


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})
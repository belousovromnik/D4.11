
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, PubHouse
from django.shortcuts import redirect


def home(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_list(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def author_list(request):
    template = loader.get_template('author_list.html')
    author = Author.objects.all()
    biblio_data = {
        "objects_list": author,
    }
    return HttpResponse(template.render(biblio_data, request))

def pubhouse_list(request):
    template = loader.get_template('pubhouse_list.html')
    pubhouse = PubHouse.objects.all().order_by('name')

    cont = []
    for item in pubhouse:
        books = Book.objects.filter(pubhouse=item.id).order_by('author__full_name', 'title')
        c_inc = []
        for book in books:
            c_inc.append(book.author.full_name + ' - ' + book.title)

        pub_inc = {}
        pub_inc[item.name] = c_inc
        cont.append(pub_inc)

    biblio_data = {
        "objects_list": cont,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            book.copy_count += 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')

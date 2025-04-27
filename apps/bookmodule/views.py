from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count
from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from .models import Address
from .models import Student
from .models import Department
from .models import Course
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm


def index(request):
      return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def html5_links(request):
    return render(request, "bookmodule/links.html")

def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def add_book():
    book = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120, edition=3)
    book.save()

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='ms').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & ~(
            Q(title__icontains='co') | Q(author__icontains='co')
        )
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    city_counts = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'city_counts': city_counts})

def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9_task1.html', {'departments': departments})

def lab9_task2(request):
    courses = Course.objects.annotate(num_students=Count('students'))
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses})

def lab9_task3(request):
    departments = Department.objects.annotate(oldest_id=Min('students__id'))
    return render(request, 'bookmodule/lab9_task3.html', {'departments': departments})


def lab9_task4(request):
    departments = Department.objects.annotate(num_students=Count('students')).filter(
        num_students__gt=2).order_by('-num_students')

    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('list_books')  # اسم المسار حق task 1
    return render(request, 'bookmodule/lab9_part1_add.html')

def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('list_books')
    
    return render(request, 'bookmodule/lab9_part1_edit.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')

def lab9_part2_list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2_list.html', {'books': books})

def lab9_part2_add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_list_books')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2_add.html', {'form': form})

def lab9_part2_edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_edit.html', {'form': form, 'book': book})

def lab9_part2_delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('lab9_part2_list_books')
    return render(request, 'bookmodule/lab9_part2_confirm_delete.html', {'book': book})
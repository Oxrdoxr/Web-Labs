from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.html5_links, name="books.html5_links"),
    path('html5/text/formatting/', views.text_formatting, name="books.text_formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('search/', views.search_books, name="books.search_books"),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='task7'),
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('lab9_part2/listbooks', views.lab9_part2_list_books, name='lab9_part2_list_books'),
    path('lab9_part2/addbook', views.lab9_part2_add_book, name='lab9_part2_add_book'),
    path('lab9_part2/editbook/<int:id>', views.lab9_part2_edit_book, name='lab9_part2_edit_book'),
    path('lab9_part2/deletebook/<int:id>', views.lab9_part2_delete_book, name='lab9_part2_delete_book'),
    path('students/list/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('lab11_part2/liststudents', views.list_students2, name='list_students2'),
    path('lab11_part2/addstudent', views.add_student2, name='add_student2'),
    path('lab11_part2/editstudent/<int:id>/', views.edit_student2, name='edit_student2'),
    path('lab11_part2/deletestudent/<int:id>/', views.delete_student2, name='delete_student2'),
    path('lab11_part3/addprofile', views.add_profile, name='add_profile'),
    path('lab11_part3/listprofiles', views.list_profiles, name='list_profiles'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
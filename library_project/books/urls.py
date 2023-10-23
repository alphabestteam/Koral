from django.urls import path
from . import views


urlpatterns = [
    path('addBook/', views.add_book),
    path('updateBook/', views.update_book),
    path('getBooks/', views.get_all_books),
    path('deleteBook/', views.delete_book),
    path('addBookReview/', views.add_book_review),
    path('getDescription/<int:book_id>/', views.get_description),
    path('howManyYears/<int:book_id>/', views.calculate_how_many_years_from_published),
    path('howLongReview/<int:book_id>/', views.how_long_review_description),
    path("authorName/<int:book_id>", views.MyView.get),
    
]

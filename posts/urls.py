from django.urls import path

from .views import main_page, DownloadBookView, add_comment_to_post, novelty, random_book, UpdateBookView, DeleteBookView

urlpatterns = [
    path('', main_page, name='main_page'),
    path('novelty/', novelty, name='novelty'),
    path('what_to_read/', random_book, name='what_to_read'),
    path('add/', DownloadBookView.as_view(), name='upload_book'),
    path('post/<int:pk>/update/', UpdateBookView.as_view(), name='update_book'),
    path('post/<int:pk>/delete/', DeleteBookView.as_view(), name='book_delete'),
    path('post/<int:pk>/', add_comment_to_post, name='book_detail'),

]

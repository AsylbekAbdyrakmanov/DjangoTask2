from django.shortcuts import render, redirect
import random
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import BookForm, CommentForm
from .models import Post


def main_page(request):
    posts = Post.objects.all()
    return render(request, 'base.html', {'posts': posts})


def novelty(request):
    posts = Post.objects.filter(published=True).order_by('-published_date')[0:5]  # выводит максимум 5 новых книг
    return render(request, 'novelty.html', {'posts': posts})


class DownloadBookView(CreateView):
    model = Post
    form_class = BookForm
    success_url = reverse_lazy('main_page')
    template_name = 'upload_book.html'


class UpdateBookView(UpdateView):
    model = Post
    form_class = BookForm
    success_url = reverse_lazy('main_page')
    template_name = 'update_book.html'


class DeleteBookView(DeleteView):
    model = Post
    success_url = reverse_lazy('main_page')
    template_name = 'book_delete.html'


def add_comment_to_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'book_detail.html', {'post': post, 'form': form})


# Функция которая возвращает рандомные книги если книг больше 3-х !!!!Книг должно быть больше 3-х
def random_book(request):
    items = Post.objects.all()
    posts = random.sample(list(items), 3)
    return render(request, 'what_to_read.html', {'posts': posts})



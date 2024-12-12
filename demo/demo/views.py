from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from falco.htmx import for_htmx
from falco.pagination import paginate_queryset
from falco.types import HttpRequest

from .forms import AuthorForm
from .forms import BookForm
from .models import Author
from .models import Book


@for_htmx(use_partial="table")
def author_list(request: HttpRequest):
    authors = Author.objects.order_by("-created_at")
    return TemplateResponse(
        request,
        "demo/author_list.html",
        context={
            "authors_page": paginate_queryset(request, authors),
            "fields": ("id", "first_name", "last_name", "birth_date"),
        },
    )


def author_detail(request: HttpRequest, pk):
    author = get_object_or_404(Author.objects, pk=pk)
    return TemplateResponse(
        request,
        "demo/author_detail.html",
        context={"author": author},
    )


def process_author_form(request: HttpRequest, pk=None):
    instance = get_object_or_404(Author.objects, pk=pk) if pk else None
    form = AuthorForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(
            reverse("demo:author_detail", args=(pk,))
            if pk
            else reverse("demo:author_list")
        )
    return TemplateResponse(
        request,
        "demo/author_form.html",
        context={"instance": instance, "form": form},
    )


@require_http_methods(["DELETE", "POST"])
def author_delete(request: HttpRequest, pk):
    Author.objects.filter(pk=pk).delete()
    return HttpResponse() if request.htmx else redirect("demo:index")


@for_htmx(use_partial="table")
def book_list(request: HttpRequest):
    books = Book.objects.order_by("-created_at")
    return TemplateResponse(
        request,
        "demo/book_list.html",
        context={
            "books_page": paginate_queryset(request, books),
            "fields": (
                "id",
                "title",
                "author",
                "published_date",
                "isbn",
                "description",
            ),
        },
    )


def book_detail(request: HttpRequest, pk):
    book = get_object_or_404(Book.objects, pk=pk)
    return TemplateResponse(
        request,
        "demo/book_detail.html",
        context={"book": book},
    )


def process_book_form(request: HttpRequest, pk=None):
    instance = get_object_or_404(Book.objects, pk=pk) if pk else None
    form = BookForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(
            reverse("demo:book_detail", args=(pk,)) if pk else reverse("demo:book_list")
        )
    return TemplateResponse(
        request,
        "demo/book_form.html",
        context={"instance": instance, "form": form},
    )


@require_http_methods(["DELETE", "POST"])
def book_delete(request: HttpRequest, pk):
    Book.objects.filter(pk=pk).delete()
    return HttpResponse() if request.htmx else redirect("demo:index")

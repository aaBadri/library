from django.urls import include, path

from books.views import BookListView


urlpatterns = [
    path("", BookListView.as_view(), name="home"),
]

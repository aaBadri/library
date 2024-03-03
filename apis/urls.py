from django.urls import include, path
from apis.views import BookApiView

urlpatterns = [
    path("", BookApiView.as_view(), name="book_list"),
]
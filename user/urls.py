from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.account),
    path("return/<str:book_id>/", views.return_book),
]
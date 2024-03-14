from django.urls import path
from . import views

urlpatterns = [
    path("info/<str:book_id>/", views.info),
    path("search/title/<str:book_name>/", views.search),
    path("function/borrow/<str:book_id>/", views.borrow),
    path("function/comment/<str:book_id>/", views.comment),
    path("function/rate/<str:book_id>/<str:rating>/", views.rate),
]
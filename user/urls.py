from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.account),
    path("return/<str:book_id>/", views.return_book),

    path("admin/add/", views.add),
    path("admin/remove/", views.remove),
    path("admin/update/", views.update),
    path("admin/updater/<str:book_id>/", views.updater),
    path("admin/return/", views.returnBook),
    path("admin/lent/", views.lent),

    path("super/add/", views.superadd),
    path("super/remove/", views.superremove),
    path("super/ban/", views.superban),
]
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import flux, posts, make_ticket, make_review, make_review_ticket, edit_ticket, edit_review

urlpatterns = [
    path('flux/', flux, name="flux"),
    path('posts/', posts, name="posts"),
    path('maketicket/', make_ticket, name='make_ticket'),
    path('<int:ticket_id>/makereview/', make_review, name='make_review'),
    path('makereviewticket/', make_review_ticket, name='make_review_ticket'),
    path('<int:ticket_id>/editticket/', edit_ticket, name='edit_ticket'),
    path('<int:review_id>/editreview/', edit_review, name='edit_review'),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import flux, make_ticket, make_review, make_review_ticket

urlpatterns = [
    path('flux/', flux, name="flux"),
    path('maketicket/', make_ticket, name='make_ticket'),
    path('makereview/', make_review, name='make_review'),
    path('makereviewticket/', make_review_ticket, name='make_review_ticket'),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
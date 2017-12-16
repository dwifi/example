from django.conf.urls import url

from invoices.views import invoice_view
from django.contrib import admin

from django.conf import settings                     #code for adding bootstrap
from django.conf.urls.static import static             #code for adding bootstrap




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', invoice_view),
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
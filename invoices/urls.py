from django.conf.urls import url
from .views import invoice_view



app_name = 'invoices'
urlpatterns = [

    url(r'^createform/$', invoice_view, name='createform'),


]

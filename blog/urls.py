from django.urls import path
from . import views #доступны все функции с файла views.py


urlpatterns = [
    path('', views.main_site, name='main_site'), 
    path('economic/',views.economic_info, name='economic_info'),#www.google.com/economic
    path('document/',views.doc_info,name='doc_info'),
    path('contact/',views.contact_info,name='contact'),
]


from unittest.mock import patch

from django.conf.urls import url
from .views import ContactView,MessageView
from django.urls import path
urlpatterns=[
    path('', ContactView.as_view(), name='contact_form'),
    path('xabarlar/',MessageView.as_view(),name='xabarlar'),
]
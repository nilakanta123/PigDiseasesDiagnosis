from django.urls import path
from .views import page_one

urlpatterns = [
    path('', page_one, name='page_one'),
    # path('ajax_request/', ajax_request),
]
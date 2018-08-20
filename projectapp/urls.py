from django.urls import path
from .views import page_am, page_pm

urlpatterns = [
	path('', page_am, name='page_am'),
    path('antimortem/', page_am, name='page_am'),
    path('postmortem/', page_pm, name='page_pm'),
]
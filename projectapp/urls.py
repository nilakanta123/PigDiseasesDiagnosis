from django.urls import path
from .views import page_am, page_pm, page_pm_result, page_am_result

urlpatterns = [
    path('', page_am, name='page_am'),
    path('antimortem/', page_am, name='page_am'),
    path('postmortem/', page_pm, name='page_pm'),
    path('antimortem/result/', page_am_result, name='page_am_result'),
    path('postmortem/result/', page_pm_result, name='page_pm_result'),

<<<<<<< HEAD
]
=======
]
>>>>>>> 1a5e23280bfdba7447c0c53d28fb93b9614f950d

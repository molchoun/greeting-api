"""
URLs for greeting_api.
"""
from django.urls import re_path, path  # pylint: disable=unused-import
from greeting_api import views# pylint: disable=unused-import

urlpatterns = [
    path('greeting/', views.GreetingView.as_view()),
]

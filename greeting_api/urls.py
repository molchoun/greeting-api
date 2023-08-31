"""
URLs for greeting_api.
"""
from django.urls import re_path  # pylint: disable=unused-import
from greeting_api import views# pylint: disable=unused-import

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    re_path(r'greeting/', views.GreetingView.as_view()),
]

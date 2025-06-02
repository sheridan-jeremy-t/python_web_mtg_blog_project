# conftest.py
import pytest
import os


def pytest_configure():
    from django.conf import settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtg_blog_project.settings')

    if not settings.configured:
        import django
        django.setup()
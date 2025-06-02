import pytest
from django.db import connection
from django.test.utils import override_settings

@pytest.mark.django_db
def test_db_connection():
    """Test the database connection"""
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        assert result[0] == 1
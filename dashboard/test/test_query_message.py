import pytest
from dashboard.models import Message


def test_get_messages():
    messages = Message.objects.find()
    assert messages is not None
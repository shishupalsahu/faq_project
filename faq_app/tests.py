from django.test import TestCase

# Create your tests here.
import pytest
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question='What is Django?',
        answer='Django is a high-level Python Web framework.',
    )
    assert faq.question == 'What is Django?'
    assert faq.get_question('en') == 'What is Django?'

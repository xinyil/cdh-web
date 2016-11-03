from django.core.management import call_command
from django.urls import reverse
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestIndex(TestCase):
    fixtures = ['test_index.json']

    def test_home(self,):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200
        # should render with custom template
        assert 'pages/index.html' in response.template_name
        # sanity check for expected content
        self.assertContains(response, 'Center for Digital Humanities')
        # NOTE: index page doesn't actually render fixture content
        # self.assertContains(response, 'test home page',
            # msg_prefix='home page should include test content from fixture')

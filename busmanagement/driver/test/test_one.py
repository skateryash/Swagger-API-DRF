import pytest
from django.urls import reverse
from rest_framework import status
from driver.models import Driver

@pytest.fixture
def create_driver(db):
    return Driver.objects.create(name='test driver', mobile='2131233211', age=34)

@pytest.mark.django_db
def test_get_driver_list(client, create_driver):
    url = reverse('drivers-api1')
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_create_driver(client):
    url = reverse('drivers-api1')
    data = { "name": "New Test", "mobile": "2229994545", "age": 28 }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Driver.objects.count() == 1

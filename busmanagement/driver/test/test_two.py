import pytest
from django.urls import reverse
from rest_framework import status
from driver.models import Driver

@pytest.fixture
def create_driver(db):
    return Driver.objects.create(name='test driver', mobile='2131233211', age=38)

@pytest.mark.django_db
def test_update_driver(client, create_driver):
    url = reverse('drivers-api2', kwargs={'id': create_driver.id})
    data = {"id": create_driver.id,"name": "Updated Driver", "mobile": "1111999933", "age": 33}
    response = client.put(url, data, content_type='application/json')
    
    assert response.status_code == status.HTTP_200_OK
    create_driver.refresh_from_db()
    assert create_driver.name == 'Updated Driver'

@pytest.mark.django_db
def test_delete_driver(client, create_driver):
    url = reverse('drivers-api2', kwargs={'id': create_driver.id})
    print(Driver.objects.count())
    response = client.delete(url, format='json')
    print(Driver.objects.count())
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Driver.objects.count() == 0

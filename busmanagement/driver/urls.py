from django.urls import path
from .views import views_one, views_two

urlpatterns = [
    path('api1/', views_one.DriverAPI.as_view(), name='drivers-api1'),
    path('api2/<int:id>/', views_two.DriverAPI.as_view(), name='drivers-api2'),
]

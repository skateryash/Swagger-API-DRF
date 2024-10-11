from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from driver.models import Driver
from driver.serializer import DriverSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class DriverAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    @swagger_auto_schema(
            operation_summary="Get driver(s)",
            operation_description="This endpoint allows you to retrieve all drivers or a specific driver by ID.",
            manual_parameters=[
                openapi.Parameter(
                    'id', openapi.IN_QUERY, description="Driver ID", type=openapi.TYPE_INTEGER, required=False
                )
            ],
            )
    def get(self, request):
        params = request.query_params
        if params:
            driver = Driver.objects.filter(id=params['id'])
        else:
            driver = Driver.objects.all()
        serializer = DriverSerializer(driver, many = True)
        return Response(serializer.data)

    @swagger_auto_schema(
            operation_summary="Create a new driver",
            operation_description="This endpoint allows you to create a new driver with the provided details.",
            request_body=DriverSerializer,
            )
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

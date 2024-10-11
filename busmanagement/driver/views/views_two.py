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
            operation_summary="Update an existing driver",
            operation_description="This endpoint allows you to update the details of an existing driver by ID.",
            request_body=DriverSerializer,
            )
    def put(self, request, id):
        try:
            driver = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(instance=driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            operation_summary="Delete a driver",
            operation_description="This endpoint allows you to delete an existing driver by ID.",
            manual_parameters=[
                openapi.Parameter('id', openapi.IN_PATH, description="Driver ID", type=openapi.TYPE_INTEGER, required=True)
            ],
            )
    def delete(self, request, id):
        try:
            driver = Driver.objects.get(id=id)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

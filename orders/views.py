from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Orders
from .serializers import OrdersSerializer


class OrdersListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, id=None):
    if id:
      # If an id is provided in the GET request, retrieve the Orders item by that id
      try:
        # Check if the Orders item the user wants to update exists
        queryset = Orders.objects.get(id=id)
      except Orders.DoesNotExist:
        # If the Orders item does not exist, return an error response
        return Response({'errors': 'This Orders item does not exist.'}, status=400)

      # Serialize Orders item from Django queryset object to JSON formatted data
      read_serializer = OrdersSerializer(queryset)

    else:
      # Get all Orders items from the database using Django's model ORM
      queryset = Orders.objects.all()

      # Serialize list of Orderss item from Django queryset object to JSON formatted data
      read_serializer = OrdersSerializer(queryset, many=True)

    # Return a HTTP response object with the list of Order items as JSON
    return Response(read_serializer.data)


  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = OrderSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new Orders item record in the database
      Orders_item_object = create_serializer.save()

      # Serialize the new Orders item from a Python object to JSON format
      read_serializer = OrdersSerializer(Orders_item_object)

      # Return a HTTP response with the newly created Orders item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the Orders item the user wants to update exists
      Orders_item = Orders.objects.get(id=id)
    except Order.DoesNotExist:
      # If the Orders item does not exist, return an error response
      return Response({'errors': 'This Orders item does not exist.'}, status=400)

    # If the Order item does exists, use the serializer to validate the updated data
    update_serializer = OrderSerializer(Order_item, data=request.data)

    # If the data to update the Order item is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the Orders item in the database
      Orders_item_object = update_serializer.save()

      # Serialize the Orders item from Python object to JSON format
      read_serializer = OrdersSerializer(Orders_item_object)

      # Return a HTTP response with the newly updated Orders item
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the Orders item the user wants to update exists
      Orders_item = Orders.objects.get(id=id)
    except Order.DoesNotExist:
      # If the Orders item does not exist, return an error response
      return Response({'errors': 'This Orders item does not exist.'}, status=400)

    # Delete the chosen Order item from the database
    Order_item.delete()

    # Return a HTTP response notifying that the Order item was successfully deleted
    return Response(status=204)
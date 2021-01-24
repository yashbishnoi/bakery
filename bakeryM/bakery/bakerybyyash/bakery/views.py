from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BakeryItem, Order
from bakery.serializers import UserSerializer, BakeryItemSerializer,OrderSerializer
from django.contrib.auth.models import User
from bakery.services import logging_in_service
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import request


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


@api_view(['POST'])
def register(request):
    """
    Registeration form
    """
    try:
        if request.method == "POST":
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                
                response = serializer.save()
                if response:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """
    Login
    """
    try:
        if request.method == "POST":
            data=request.data
            response= logging_in_service(request,**data)
            username=data.get('username')
            password=data.get('password')
            if response:
                return Response(f"Hi {username}! Please generate token", status=status.HTTP_200_OK)
            else:
                raise Exception
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_item(request):
    """
    Get all bakery items
    """
    try:
        if request.method == "GET":
            serializer=BakeryItemSerializer(BakeryItem.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_item(request):
    """
    Order bakery items
    """
    try:
        if request.method == "POST":
            serializer=OrderSerializer(data=request.data)
            if serializer.is_valid():
                response, order_status = serializer.save(request)
                if order_status:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(response.get("error"), status=status.HTTP_400_BAD_REQUEST)    
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_order_history(request):
    """
    Get order history
    """
    try:
        if request.method == "GET":
            serializer=OrderSerializer(Order.objects.filter(user=request.user), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


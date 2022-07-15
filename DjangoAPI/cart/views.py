from django.http import Http404
from django.shortcuts import render

from cart.models import Cart, Items
from cart.serializers import CartItemSerializer, CartSerializer, CartSerializer
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response 
# Create your views here.

class CarttView(APIView):
    
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Cart.objects.filter(category__category_name =  category)
        else:
            queryset = Cart.objects.all()
        serializer = CartSerializer(queryset , many = True)
        return Response({'count' : len(serializer.data) ,'data' :serializer.data})


class CartDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CartSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CartSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCartDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Items.objects.get(user=pk)
        except Items.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CartItemSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CartItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
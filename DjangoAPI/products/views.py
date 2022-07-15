from django.http import Http404
from django.shortcuts import render

from .serializers import *
from .models import *
# Create your views here.
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

# class DemoView(APIView):
#      permission_classes = [IsAuthenticated]
#      def get(self ,request):
#          print(request.user)
#          return Response({'sucess' : "Hurray you are authenticated"})
    

class ProductView(APIView):
    
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name =  category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset , many = True)
        return Response({'count' : len(serializer.data) ,'data' :serializer.data})

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
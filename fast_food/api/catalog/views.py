from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from catalog.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer



class CategoryView(APIView):

    def get(self, request, format=None):

        category = get_object_or_404(Category, id=3)
        serializer = CategorySerializer(category)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.create(serializer.data)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductView(APIView):

    def get(self, request, format=None):

        product = Product.objects.all()
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.create(serializer.data)
        serializer = ProductSerializer(category)
        return Response(serializer.data)

class ListProduct(generics.ListAPIView, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes  = [JSONParser]

class ListCategories(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes  = [JSONParser, FormParser]


class OneCategories(generics.RetrieveAPIView,
                    generics.UpdateAPIView, generics.DestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fields = ['id']

    def get_object(self):
        print( self.kwargs['id'])
        obj = get_object_or_404(Category, id=self.kwargs['id'])
        return obj


# class ListCategories(APIView):
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         categories = [category.name for category in Category.objects.all()]
#
#         return Response(categories)
#
#     def post(self, request, format=None):
#
#         return Response({'success': 'OK'})


class ListCategories(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes  = [JSONParser, FormParser]


class OneCategories(generics.RetrieveAPIView,
                    generics.UpdateAPIView, generics.DestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_fields = ['id']

    def get_object(self):
        print( self.kwargs['id'])
        obj = get_object_or_404(Category, id=self.kwargs['id'])
        return obj


# class ListCategories(APIView):
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         categories = [category.name for category in Category.objects.all()]
#
#         return Response(categories)
#
#     def post(self, request, format=None):
#
#         return Response({'success': 'OK'})




# ViewSets define the view behavior.
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

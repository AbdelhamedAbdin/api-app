from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, authentication, viewsets
from rest_framework.generics import mixins
from .authentication import TokeAuthentication

from .serializers import ProductSerializer, PostSerializer
from .models import Product, Post
from django.shortcuts import get_object_or_404, get_list_or_404


# @api_view(["GET"])
# def products(request):
#     product = Product.objects.all().order_by("?").first()
#     # product_objects = {}
#     data = {}
#
#     if product:
#         data = ProductSerializer(product)
#         print(data.data)
#     return Response(data.data)


# @api_view(["POST"])
# def products(request):
#     data = request.data
#     serializer = ProductSerializer(data=data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data)

# class ProductListApiView(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

# class ProductListApiView(generics.CreateAPIView):
#     serializer_class = ProductSerializer
#
#
class ProductApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [TokeAuthentication]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if title and content is None:
            content = title
        serializer.save(content=content)
        return super(ProductApiView, self).perform_create(serializer)


class GetProduct(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

# @api_view(["GET", "POST"])
# def function_api_view(request, pk=None, *args, **kwargs):
#     method = request.method
#
#     if method == "GET":
#         if pk:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
#
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
#             if title and content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)

class PostView(viewsets.GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'


    def list(self, request, *args, **kwargs):
        posts = self.serializer_class(self.queryset, many=True)
        print(posts.data)
        return Response(data=posts.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

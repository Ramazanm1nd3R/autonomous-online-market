from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Overview of all product-related endpoints",
    responses={200: "API Overview"}
)
def api_overview(request):
    api_urls = {
        'List': '/product/',
        'Detail View': '/product/<int:pk>/',
        'Create': '/product/create/',
        'Update': '/product/update/<int:pk>/',
        'Delete': '/product/delete/<int:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="List all products",
    responses={200: ProductSerializer(many=True)}
)
def view_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Get details of a specific product by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Product ID", type=openapi.TYPE_INTEGER)
    ],
    responses={200: ProductSerializer()}
)
def view_product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Add a new product",
    request_body=ProductSerializer,
    responses={201: ProductSerializer(), 400: "Validation errors"}
)
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Update a product by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Product ID", type=openapi.TYPE_INTEGER)
    ],
    request_body=ProductSerializer,
    responses={200: ProductSerializer(), 400: "Validation errors"}
)
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Delete a product by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Product ID", type=openapi.TYPE_INTEGER)
    ],
    responses={204: "No Content"}
)
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="List all categories",
    responses={200: CategorySerializer(many=True)}
)
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Get details of a specific category by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER)
    ],
    responses={200: CategorySerializer()}
)
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Create a new category",
    request_body=CategorySerializer,
    responses={201: CategorySerializer(), 400: "Validation errors"}
)
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Update a category by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER)
    ],
    request_body=CategorySerializer,
    responses={200: CategorySerializer(), 400: "Validation errors"}
)
def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@swagger_auto_schema(
    operation_description="Delete a category by ID",
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER)
    ],
    responses={204: "No Content"}
)
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

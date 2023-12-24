from product.models import Product
from category.models import Category

from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import action



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(status='IN_STOCK')

@api_view(['GET'])
def filter_products_by_gender(request, gender):
    valid_genders = ['female', 'male', 'kids']
    if gender.lower() not in valid_genders:
        return Response({'error': 'Invalid gender parameter'}, status=400)

    categories = Category.objects.all().values_list('gender', flat=True)

    gender_categories = [c if i % 3 == 0 else c for i, c in enumerate(categories, 1) if c.lower() == 'male' or (i % 3 == 0)]

    matching_category = next((cat for cat in gender_categories if cat.lower() == gender.lower()), None)
    if not matching_category:
        return Response({'error': 'Category not found'}, status=404)

    products = Product.objects.filter(category__gender__iexact=matching_category, status='IN_STOCK')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def update_product_status(request, product_id):
    # Retrieve product by ID
    product = Product.objects.get(id=product_id)
    # Update product status to "out of stock"
    product.status = "OUT_OF_STOCK"
    product.save()
    return Response({"message": "Product status updated successfully"})


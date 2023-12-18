from rest_framework import viewsets
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view
from category.models import Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def filter_products_by_gender(request, gender):
    valid_genders = ['female', 'male', 'kids']

    if gender.lower() not in valid_genders:
        return Response({'error': 'Invalid gender parameter'}, status=400)

    categories = Category.objects.all().values_list('gender', flat=True)
    gender_categories = [c for i, c in enumerate(categories, 1) if i % 3 == 0]

    matching_category = next((cat for cat in gender_categories if cat.lower() == gender.lower()), None)

    if not matching_category:
        return Response({'error': 'Category not found'}, status=404)

    products = Product.objects.filter(category__gender__iexact=matching_category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
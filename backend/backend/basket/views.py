from basket.models import Basket
from basket.serializers import BasketSerializer
from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

@api_view(['POST'])
def add_to_basket(request):
    user_id = request.data.get('user_id')
    product_ids = request.data.get('product_ids')
    # Retrieve products based on product_ids
    products = Product.objects.filter(id__in=product_ids)
    # Create a basket entry for the user
    basket = Basket.objects.create(user_id=user_id, number_of_products=len(products))
    basket.products.add(*products)
    basket.total_price = sum(product.price for product in products)
    basket.save()
    return Response({"message": "Products added to the basket successfully"})


@api_view(['POST'])
def checkout(request):
    user = request.user  # Assuming the user is authenticated

    # Get the user's current basket
    current_basket = Basket.objects.filter(user_id=user.id).first()

    if current_basket:
        # Update product status in the current basket
        products_in_basket = current_basket.products.all()
        for product in products_in_basket:
            product.status = 'OUT_OF_STOCK'  # Update product status to "out of stock"
            product.save()

        # Add current basket to user's shopping history
        user.shopping_history.add(current_basket)

        # Create a new basket for the user
        new_basket = Basket.objects.create(user_id=user.id)
        
        return Response({'message': 'Checkout successful'})
    else:
        return Response({'error': 'No items in the basket'}, status=400)
from django.http import JsonResponse
from basket.models import Basket
from basket.serializers import BasketSerializer
from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from user.models import User

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    @action(detail=False, methods=['POST'])
    def add_to_basket(self, request):
    
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')

        if not user_id or not product_id:
            return JsonResponse({"error": "Invalid data provided"}, status=400)

        product = Product.objects.filter(id=product_id).first()

        if product == None:
            return JsonResponse({"error": "Product not found"}, status=404)

        user = User.objects.get(id=user_id)
        # Check if a basket already exists for the user
        basket = Basket.objects.filter(user_id=user).first()

        if basket:
            basket.number_of_products += 1
            basket.product.add(product)
            basket.total_price += product.price
            basket.save()
        else:
            new_basket = Basket.objects.create(user_id=user, number_of_products=1)
            new_basket.products.add(product)
            new_basket.total_price = product.price
            new_basket.save()

        return JsonResponse({"message": "Product added to the basket successfully"})

        

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
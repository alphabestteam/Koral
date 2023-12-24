from basket.models import Basket
from basket.serializers import BasketSerializer
from product.models import Product
from user.models import User

from django.http import JsonResponse
from decimal import Decimal
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action



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

        if product is None:
            return JsonResponse({"error": "Product not found"}, status=404)

        user = User.objects.get(id=user_id)
        basket = Basket.objects.filter(user_id=user).first()

        if basket:
            # Check if the product is already in the basket
            product_in_basket = basket.product.filter(id=product_id).first()

            if product_in_basket:
                product_in_basket.quantity += 1
                product_in_basket.save()
                basket.number_of_products += 1
                print(basket.number_of_products)
                basket.total_price += Decimal(str(product.price))
                basket.save()
                print("here")
            else:
                # If the product doesn't exist in the basket, add it and update quantity and total price
                basket.product.add(product)
                product.save()

                basket.number_of_products += 1
                basket.total_price += product.price
                basket.save()
        else:
            # Create a new basket and add the product
            new_basket = Basket.objects.create(user_id=user, number_of_products=1)
            new_basket.product.add(product)
            new_basket.total_price = Decimal(str(product.price))
            product.save()
            new_basket.save()            
        return JsonResponse(
            {"message": "Product added to the basket successfully"})
    

    @action(detail=False, methods=['DELETE'])
    def delete_from_basket(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')

        if not user_id or not product_id:
            return JsonResponse({"error": "Invalid data provided"}, status=400)
        product = Product.objects.filter(id=product_id).first()

        if product is None:
            return JsonResponse({"error": "Product not found"}, status=404)

        user = User.objects.get(id=user_id)
        basket = Basket.objects.filter(user_id=user).first()
        if basket:
            # Check if the product is in the basket
            product_in_basket = basket.product.filter(id=product_id).first()

            if product_in_basket:
                # Reduce the quantity of the product and update basket information
                if product_in_basket.quantity <= 1:
                    basket.product.remove(product)
                else:
                    product_in_basket.quantity -= 1

                product_in_basket.save()

                basket.number_of_products -= 1
                basket.total_price -= Decimal(str(product.price))
                basket.save()
                
                return JsonResponse({"message": "Product removed from the basket successfully"}, status=200)
            else:
                return JsonResponse({"error": "Product not found in the basket"}, status=404)
        else:
            return JsonResponse({"error": "Basket not found"}, status=404)
        

@api_view(['GET'])        
def get_total_price(request, user_id):
    if user_id is None:
        return Response({"error": "User ID is required"}, status=400)

    try:
        user = User.objects.get(id=user_id)
        basket = Basket.objects.filter(user_id=user).first()

        if basket is None:
            return Response({"error": "Basket not found"}, status=404)
        
        total_price_decimal = Decimal(str(basket.total_price)) 
        return Response({"total_price": total_price_decimal}, status=200)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['POST'])
def checkout(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if user_id is None:
            return Response({"error": "User ID is required"}, status=400)
    
    # Get the user's current basket
    current_basket = Basket.objects.filter(user_id=user_id).first()

    if current_basket:
        # Update product status in the current basket
        products_in_basket = current_basket.product.all()
        for product in products_in_basket:
            product.status = 'OUT_OF_STOCK'  # Update product status to "out of stock"
            product.quantity = 1
            product.save()         

        # Add current basket to user's shopping history
        user.shopping_history.add(current_basket)
        current_basket.total_price = 0
        current_basket.product.clear()
        current_basket.save()
        
        return Response({'message': 'Checkout successful'}, status=200)
    else:
        return Response({'error': 'No items in the basket'}, status=400)
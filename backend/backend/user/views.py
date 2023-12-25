from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from basket.models import Basket
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import action
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username is already taken'}, status=400)

        user = User.objects.create(username=username, password=password)
        user.save()
        return JsonResponse({'message': 'User registered successfully'}, status=201)


    @action(detail=False, methods=['POST'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the username exists in the database
        user = User.objects.filter(username=username).first()

        if user:
            # If the user exists, check the provided password
            if password == user.password:
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'message': 'Password is wrong'}, status=401)
        else:
            return JsonResponse({'message': 'User not found'}, status=404)
                

    @action(detail=False, methods=['POST'])
    def get_user_id_from_username(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            user = User.objects.get(username=username)
            return JsonResponse({'userId': user.id})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
        
    
    @action(detail=True, methods=['put'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('new_password')
        
        if new_password:
            user.password = new_password
            user.save()
            return Response({'message': 'Password updated successfully'}, status=200)
        else:
            return Response({'error': 'New password not provided'}, status=400)


@api_view(['GET'])        
def get_products_in_basket(request, basket_id):
    user_basket = get_object_or_404(Basket, basket_id=basket_id)
    
    user_products = user_basket.product.all()    
    products_data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'status': product.status,
            'picture': product.picture.url,
            'quantity': product.quantity
        }
        for product in user_products
    ]

    return JsonResponse(products_data, safe=False)


@api_view(['GET'])
def get_current_basket_id(request, user_id):
    current_basket = Basket.objects.filter(user_id=user_id).first()
    if current_basket:
        return JsonResponse({'basket_id': current_basket.basket_id})
    else:
        return JsonResponse({'error': 'Basket not found'}, status=404)
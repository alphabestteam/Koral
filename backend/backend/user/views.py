from django.http import JsonResponse
from rest_framework import viewsets
from basket.models import Basket
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import action
import json
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
        
        
    action(detail=False, methods=['GET'])
    def get_products_in_basket(self, request):
        user = self.request.user
        try:
            basket = Basket.objects.get(user_id=user.id)
            user_products = basket.products.all()  # Assuming 'products' is a related field in your Basket model
            # Process user_products as needed or return it in the response
            # Assuming 'products' is a list of products associated with the basket
            product_ids = [product.id for product in user_products]
            return Response(product_ids)  # Returning IDs for demonstration, adjust as needed
        except Basket.DoesNotExist:
            return Response({"error": "Basket does not exist"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)    
        
        
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
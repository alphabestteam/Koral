from django.http import JsonResponse
from rest_framework import viewsets
from basket.models import Basket
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import action
from django.db.models.signals import post_save
from django.dispatch import receiver



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
    def get_queryset(self):
        # Get the current authenticated user
        user = self.request.user

        # Fetch products associated with the user's basket
        user_products = Basket.objects.filter(user_id=user.id).values_list('product', flat=True)
        
        return user_products


@receiver(post_save, sender=Basket)
def update_shopping_history(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if user and isinstance(user, User):
            if hasattr(user, 'shopping_history'):
                user.shopping_history.add(instance)
            else:
                # Handle the case where shopping_history doesn't exist
                print("User has no shopping_history attribute")
        else:
            # Handle the case where user is None or not a valid User object
            print("Invalid user or user is None")
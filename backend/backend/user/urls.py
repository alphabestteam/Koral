from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/<int:basket_id>/get_products_in_basket/', views.get_products_in_basket, name='get_products_in_basket'),
    path('api/users/<int:user_id>/get_current_basket_id/', views.get_current_basket_id, name='get_current_basket_id'),
]
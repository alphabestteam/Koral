from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'Basket', views.BasketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('add_to_basket/', views.add_to_basket),
    path('checkout/', views.checkout)

]
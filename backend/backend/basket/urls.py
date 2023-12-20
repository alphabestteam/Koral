from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'Basket', views.BasketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('<int:user_id>/checkout/', views.checkout),
    path('<int:user_id>/get_total_price/', views.get_total_price)
]
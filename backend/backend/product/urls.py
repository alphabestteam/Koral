from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('<str:gender>/', views.filter_products_by_gender),
    path('update_product_status/<int:product_id>/', views.update_product_status),

]
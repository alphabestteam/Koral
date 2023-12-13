from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'Basket', views.BasketViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('user_basket/<int:user_id>/', views.user_basket),

]
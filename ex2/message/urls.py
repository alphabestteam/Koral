from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'message', views.MessageViewSet)
router.register(r'send_message', views.SendMessageViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]

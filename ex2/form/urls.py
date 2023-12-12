from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'Form', views.UserViewSet)
router.register(r'FileSharingForm', views.FileSharingViewSet)
router.register(r'MessagesForm', views.MessagesViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

]

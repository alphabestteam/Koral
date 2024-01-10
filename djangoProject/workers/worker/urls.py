from django.urls import path
from . import views

urlpatterns = [
    path('get_workers/', views.get_workers),
    path('add_worker/', views.add_worker),
    path('update_worker/<int:worker_id>/', views.update_worker),
    path('delete_worker/<int:worker_id>/', views.delete_worker),
]

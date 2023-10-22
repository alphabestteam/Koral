from django.urls import path

from . import views

urlpatterns = [
    path('AddTarget/', views.add_target),
    path('UpdateTarget/', views.update_target),
    path('AllTargets/', views.all_targets)
    # Add here all the URLs you need

]

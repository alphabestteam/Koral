"""
URL configuration for personProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/getAllPeople/', views.get_all_people),
    path('api/addPerson/', views.add_person),
    path('api/removePerson/<int:id_number>/', views.remove_person),
    path('api/updatePerson/', views.update_person),
    path('api/getAllParents/' ,views.get_all_parents),
    path('api/addParent/' ,views.add_parent),
    path('api/removeParent/<int:id_number>/', views.remove_parent),
    path('api/updateParent/', views.update_parent),
    path('api/connectChild/', views.connect_child),
    path('api/ParentInfo/<int:id_number>/', views.parent_info),
    path('api/RichChildren/', views.rich_children),
    path('api/ParentsName/<int:id_number>/', views.parents_names),
    path('api/ChildrenInfo/<int:id_number>/', views.children_information),
    path('api/GrandparentsInfo/<int:id_number>/', views.grandparents_information),
    path('api/BrothersInfo/<int:id_number>/', views.brothers_information),
    

    

#need to add the other api's

]

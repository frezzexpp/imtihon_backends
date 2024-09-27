from food.views import *
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    #food:
    path('admin/', admin.site.urls),
    path('food-post/', FoodPostAuthentication.as_view()),
    path('food-retrieve-get/<int:pk>/', FoodRetrieveGet.as_view()),
    path('food-update-owner/', FoodUpdateOwner.as_view()),
    path('food-patch/<int:pk>/', FoodPatch.as_view()),
    path('food-destroy/', FoodDestroy.as_view()),
    path('food-get/', GetFood.as_view()),


    #category:
    path('category-post/', CategoryCreate.as_view()),
    path('category-read/<int:pk>/', CategoryRead.as_view()),
    path('category-update-owner/', CategoryUpdateOwner.as_view()),
    path('category-destroy/', CategoryDeleteAdmin.as_view()),
    path('category-read/<int:pk>/', CategoryRead.as_view()),
    path('category-list/<int:pk>/', CategoryList.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from food.models import Food,Category
from food.serializers import *
from food.permision import *


#FOOD:
#1-Create a food
class FoodPostAuthentication(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAuthenticated, )


#2-Get a food from id:
class FoodRetrieveGet(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            try:
                instance = Food.objects.get(pk=pk)

            except Food.DoesNotExist:
                return Response({"Answer": "Data not found!"})

            serializer = FoodSerializersApi(instance)
            return Response({"Person": serializer.data})


#3-update food only owner:
class FoodUpdateOwner(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsOwner, )



#4-food patch
class FoodPatch(APIView):
    def patch(self, request, *args, **kwargs):

        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Answer": "Metod Patch not allowed!"})
        try:
            instance = Food.objects.get(pk=pk)

        except:
            return Response({"Answer": "Data not found"})

        serializers = FoodSerializersApi(data=request.data, instance=instance, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"Person": serializers.data})


#5-food delete only admin:
class FoodDestroy(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAdminUser, )



#6-Read list all the foods
class GetFood(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


#CATEGORY:


#1-category Create :
class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAuthenticated, )


#2- category read:
class CategoryRead(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            try:
                instance = Category.objects.get(pk=pk)

            except Category.DoesNotExist:
                return Response({"Answer": "Data not found!"}, )

            serializer = CategorySerializersApi(instance)
            return Response({"Person": serializer.data})


#3- update category:
class CategoryUpdateOwner(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsOwner, )



#4- category delete:
class CategoryDeleteAdmin(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAdminUser,)


#5- category get list:
class CategoryList(APIView):
    def get(self,request):
        list_person = Category.objects.all()
        return Response({"Persons": CategorySerializersApi(list_person, many=True).data})




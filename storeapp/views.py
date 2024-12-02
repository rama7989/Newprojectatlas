from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from storeapp.models import *



#using viewsets  crud operations are done, Viewsets are easy to  perform crud operations

class ActorViewSet(ModelViewSet):
    queryset=Actor.objects.all()
    serializer_class= ActorSerializer
  

class AddressViewSet(ModelViewSet):
    queryset=Address.objects.all()
    serializer_class= AddressSerializer
   

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer
   

class CityViewSet(ModelViewSet):
    queryset= City.objects.all()
    serializer_class= CitySerializer
    

class CountryViewSet(ModelViewSet):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer
  

class CustomerViewSet(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class= CustomerSerializer
   

class FilmViewSet(ModelViewSet):
    queryset=Film.objects.all()
    serializer_class= FilmSerializer
   

class FilmActorViewSet(ModelViewSet):
    queryset=FilmActor.objects.all()
    serializer_class= FilmActorSerializer
   

class FilmCategoryViewSet(ModelViewSet):
    queryset=FilmCategory.objects.all()
    serializer_class= FilmCategorySerializer
  

class InventoryViewSet(ModelViewSet):
    queryset=Inventory.objects.all()
    serializer_class= InventorySerializer
    

class LanguageViewSet(ModelViewSet):
    queryset=Language.objects.all()
    serializer_class= LanguageSerializer
    

class PaymentiewSet(ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class= PaymentSerializer
    

class RentalViewSet(ModelViewSet):
    queryset=Rental.objects.all()
    serializer_class= RentalSerializer
    

class StaffViewSet(ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class= StaffSerializer
    

class StoreViewSet(ModelViewSet):
    queryset=Store.objects.all()
    serializer_class= StoreSerializer
    
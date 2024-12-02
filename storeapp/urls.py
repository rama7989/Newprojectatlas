from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# router will automatically generates urls for our model viewsets

router=DefaultRouter()
router.register('actors',ActorViewSet)
router.register('address',AddressViewSet)
router.register('category',CategoryViewSet)
router.register('city',CityViewSet)
router.register('country',CountryViewSet)
router.register('customer',CustomerViewSet)
router.register('films',FilmViewSet)
router.register('filmactor',FilmActorViewSet)
router.register('fcategory',FilmCategoryViewSet)
router.register('inventory',InventoryViewSet)
router.register('language',LanguageViewSet)
router.register('payment',PaymentiewSet)
router.register('rental',RentalViewSet)
router.register('staff',StaffViewSet)
router.register('store',StoreViewSet)


urlpatterns=[
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # to access the token
    path('token-refresh/',TokenRefreshView.as_view(), name='token_refresh'), # to refresh the token 
    path('token-verify/',TokenVerifyView.as_view(),name='token-verify'), # to verify the token 
    path('',include(router.urls)), # to include all the router urls 
]
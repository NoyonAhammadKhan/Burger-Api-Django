from django.urls import path
from rest_framework.routers import DefaultRouter
from BurgerApi.views import UserProfileViewSet,OrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"user", UserProfileViewSet)
router.register(r"order", OrderViewSet,basename="order")

urlpatterns =[
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
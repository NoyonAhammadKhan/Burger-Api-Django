from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from BurgerApi.models import UserProfile,Order 
from BurgerApi.serializers import UserProfileSerializer,OrderSerializer

# Create your views here.


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

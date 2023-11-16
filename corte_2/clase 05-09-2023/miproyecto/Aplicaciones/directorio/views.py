
from rest_framework import viewsets
from .models import Friend
from .serializer import FriendSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
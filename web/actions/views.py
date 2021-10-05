from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import ListFollowerSerializer
from main.models import User


class ListFollowerView(generics.ListAPIView):
    """Вывод списка подписчиков пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(users=self.request.user)


class AddFollowerView(views.APIView):
    """Добавление в подписчики"""

    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, pk):
        user = User.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)

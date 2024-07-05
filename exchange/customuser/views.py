from rest_framework import mixins, views, response, status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UpdateUserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListUpdateView(mixins.ListModelMixin,
                         mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserGetView(views.APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is True:
            return response.Response({'detail': 'user must be authenticated'}, status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(user)
        return response.Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.user.is_anonymous is True:
            return response.Response({'detail': 'user must be authenticated'}, status.HTTP_401_UNAUTHORIZED)
        pk = request.user.pk
        user = get_object_or_404(User, pk=pk)
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_200_OK)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

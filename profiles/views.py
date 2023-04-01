from .models import UserNet
from .serializers import GetUserNetSerializer
from rest_framework.generics import RetrieveAPIView


class GetUserNetView(RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer

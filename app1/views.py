from rest_framework import status
from rest_framework.response import Response
from .models import AccAdvances
from .serializers import AccAdvancesSerializer
from rest_framework import viewsets

class AccAdvancesViewSet(viewsets.ModelViewSet):
    queryset = AccAdvances.objects.all()
    serializer_class = AccAdvancesSerializer

    def create(self, request, *args, **kwargs):
        slno = request.data.get("slno")
        instance = AccAdvances.objects.filter(slno=slno).first()

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if instance else status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Student, Curs
from .serializers import StudentSerializer, CursSerializer

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        if 'an' in self.request.GET:
            an = int(self.request.GET['an'])
            return qs.filter(an=an)
        return qs

class CursViewSet(ModelViewSet):
    serializer_class = CursSerializer
    queryset = Curs.objects.all()
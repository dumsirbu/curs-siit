from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if 'an' in self.request.GET:
            an = int(self.request.GET['an'])
            return qs.filter(an=an)
        return qs
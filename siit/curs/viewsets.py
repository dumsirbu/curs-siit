from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
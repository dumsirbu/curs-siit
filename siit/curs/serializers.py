from rest_framework.serializers import ModelSerializer

from .models import Curs, Student


class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    cursuri = CursSerializer(many=True)

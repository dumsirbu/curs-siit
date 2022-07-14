from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Curs, Student


class CursSerializer(ModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"

class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    cursuri = CursSerializer(many=True)

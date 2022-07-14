from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Curs, Student


class CursSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Curs
        fields = "__all__"

class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    cursuri = CursSerializer(many=True)

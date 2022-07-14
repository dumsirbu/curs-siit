from django.utils import timezone

from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

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
    timestamp = SerializerMethodField()
    full_name = SerializerMethodField()

    def get_timestamp(self, arg):
        return timezone.now()

    def get_full_name(self, obj):
        return f"{obj.nume} {obj.prenume}"

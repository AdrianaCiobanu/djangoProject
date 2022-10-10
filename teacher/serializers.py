from rest_framework import serializers

from teacher.models import Teacher


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'department']
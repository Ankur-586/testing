from rest_framework import serializers
from StudentApp.models import Subject

class subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('Subject_name','marks','student')
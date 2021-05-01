from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "start_date", "end_date", "number_of_lectures"]


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name"]

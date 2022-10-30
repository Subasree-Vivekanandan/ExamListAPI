from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """course_name = serializers.CharField(max_length=50)
    question_number = serializers.
    total_marks = serializers.PositiveIntegerField()

    def create(self, validated_data):
        return Course.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.course_name = validated_data.get('course_name',instance.course_name)
        instance.question_number = validated_data.get('question_number',instance.question_number)
        instance.total_marks = validated_data.get('total_marks',instance.total_marks)
        instance.save()
        return instance"""

    class Meta:
        model = Course
        fields = ['id','course_name', 'question_number', 'total_marks']

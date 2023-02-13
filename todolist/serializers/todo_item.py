from rest_framework import serializers

from todolist.models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['todo', 'complete', 'id']

    def update(self, instance, validated_data):
        raise NotImplementedError


class NewTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['todo', 'complete']

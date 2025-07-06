from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Task

# Optional: For showing username in Task


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Show username instead of ID
   
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description','priority', 'status', 'due_date', 'created_at', 'updated_at', 'user'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def create(self, validated_data):
        # Inject user from request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)

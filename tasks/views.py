from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Custom pagination class
class TaskPagination(PageNumberPagination):
    page_size = 6  # Customize how many tasks per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination

    # Add filtering support
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['priority', 'status']
    ordering_fields = ['created_at', 'due_date']

    def get_queryset(self):
        # Only return tasks that belong to the logged-in user
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class TaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure the user only modifies their own tasks
        return Task.objects.filter(user=self.request.user)

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsStudent, IsSupervisor, IsAdmin

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['faculty', 'department', 'category', 'technologies', 'title']

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), IsStudent()]
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsSupervisor() | IsAdmin()]
        if self.action in ['destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)

    def perform_update(self, serializer):
        # Supervisor approves/rejects
        serializer.save(approved_by=self.request.user)

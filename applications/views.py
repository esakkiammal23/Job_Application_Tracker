from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import JobApplication
from .serializers import JobApplicationSerializer
from .permissions import IsAdminOrOwner


class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [
    IsAuthenticated,
    IsAdminOrOwner,
]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "location",
    ]

    search_fields = [
        "company",
        "position",
    ]

    ordering_fields = [
        "salary",
        "created_at",
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role == "admin":
            return JobApplication.objects.all()

        return JobApplication.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
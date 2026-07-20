from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import InterviewRound
from .serializers import InterviewRoundSerializer


class InterviewRoundViewSet(viewsets.ModelViewSet):

    serializer_class = InterviewRoundSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = [
        "result",
        "application",
    ]

    search_fields = [
        "round_name",
        "interviewer",
    ]

    queryset = InterviewRound.objects.all()
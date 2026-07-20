from rest_framework.routers import DefaultRouter
from .views import InterviewRoundViewSet

router = DefaultRouter()

router.register(
    r"interviews",
    InterviewRoundViewSet,
    basename="interviews"
)

urlpatterns = router.urls
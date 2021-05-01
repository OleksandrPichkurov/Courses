from rest_framework import routers

from .views import CourseViewSet

router = routers.DefaultRouter()

router.register("courses", CourseViewSet, basename="courses")

urlpatterns = router.urls

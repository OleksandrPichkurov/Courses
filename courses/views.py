from django.db.models import Q

from rest_framework import viewsets, filters

from .models import Course
from .serializers import CourseSerializer, CourseDetailSerializer

# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    """
    Example parameters for filtering by date: /?start_date=2021-04-01&end_date=2021-08-30
    """

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_serializer_class(self):
        if hasattr(self, "action") and self.action == "list":
            return CourseDetailSerializer
        return CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(
                Q(start_date__lt=end_date, end_date__gte=start_date)
            )
            return queryset
        else:
            return queryset

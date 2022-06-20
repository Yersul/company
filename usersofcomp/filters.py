import django_filters
from django.db.models import Q
import django_filters
from .models import CompUsers


class CompFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter()
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')

    class Meta:
        model = CompUsers
        fields = ('name', 'surname', 'salary')


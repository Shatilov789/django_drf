from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    filter_backends = [DjangoFilterBackend]

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']

from django.urls import path

from .views import (
    AdDetailView,
    ParseAdsView,
    AdListView,
)


urlpatterns = [
    path('parse-ads/', ParseAdsView.as_view(), name='parse-ads'),
    path('ads/', AdListView.as_view(), name='ad-list'),
    path('ads/<int:ad_id>/', AdDetailView.as_view(), name='ad-detail'),
]

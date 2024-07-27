from rest_framework import serializers

from .models import Ad


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'title',
            'ad_id',
        ]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'id',
            'title',
            'ad_id',
            'author',
            'views_count',
            'position'
        ]

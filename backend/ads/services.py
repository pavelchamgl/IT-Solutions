from .models import Ad
from .serializers import AdSerializer


class AdService:
    @staticmethod
    def save_ads(ads_data):
        for ad_data in ads_data:
            serializer = AdSerializer(data=ad_data)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception(serializer.errors)

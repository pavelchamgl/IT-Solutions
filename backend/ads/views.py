from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Ad
from .parsers import AdParser
from .services import AdService
from .serializers import (
    AdSerializer,
    AdsSerializer,
)


@extend_schema(
    summary="Parse and Save Ads",
    description="Parses ads from the specified URL and saves them to the database.",
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response={'message': 'string'},
            description="Data parsed and saved successfully",
            examples=[
                    OpenApiExample(
                        "Success Response",
                        value={'message': 'Data parsed and saved successfully.'},
                        response_only=True,
                        status_codes=["200"]
                    )
                ]
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response={'error': 'string'},
            description="Bad request - error in saving data",
            examples=[
                    OpenApiExample(
                        "Error Response",
                        value={'error': 'Bad request - error in saving data.'},
                        response_only=True,
                        status_codes=["400"]
                    ),
            ]
        ),
        status.HTTP_408_REQUEST_TIMEOUT: OpenApiResponse(
            response={'error': 'string'},
            description="Request timeout - error in fetching data",
            examples=[
                OpenApiExample(
                    "Error Response",
                    value={'error': 'Request timeout - error in fetching data.'},
                    response_only=True,
                    status_codes=["408"]
                ),
            ]
        ),
    },
    tags=["Ads"]
)
class ParseAdsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"

        parser = AdParser(url)
        try:
            parser.fetch_ads()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_408_REQUEST_TIMEOUT)

        try:
            AdService.save_ads(parser.ads_data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data parsed and saved successfully"}, status=status.HTTP_200_OK)


@extend_schema(
    summary="List All Ads",
    description="Returns a list of all ads in the database.",
    responses={200: AdsSerializer(many=True)},
    tags=["Ads"]
)
class AdListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


@extend_schema(
    summary="Retrieve Ad Details",
    description="Returns detailed information about a specific ad identified by its ad_id.",
    responses={200: AdSerializer()},
    tags=["Ads"]
)
class AdDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'

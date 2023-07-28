from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bow, Purchase, TimeStatistics
from .serializers import BowSerializer, PurchaseSerializer, TimeStatisticsSerializer
from django.views.decorators.csrf import csrf_exempt


class BowListView(APIView):
    @csrf_exempt  # You can keep csrf_exempt for this view
    def get(self, request):
        bows = Bow.objects.all()
        serializer = BowSerializer(bows, many=True)
        return Response(serializer.data)

    @csrf_exempt  # Add csrf_exempt for the POST method
    def post(self, request):
        serializer = BowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseView(APIView):
    @csrf_exempt
    def post(self, request):
        # Assuming the request contains the 'name' of the bow being purchased
        try:
            bow = Bow.objects.get(name=request.data['name'])
            purchase = Purchase.objects.create(bow=bow)
            return Response("Purchase successful!", status=status.HTTP_201_CREATED)
        except Bow.DoesNotExist:
            return Response("Bow not found.", status=status.HTTP_404_NOT_FOUND)


class PurchaseListView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)


class TimeStatisticsListView(APIView):
    @csrf_exempt
    def get(self, request):
        statistics = TimeStatistics.objects.all()
        serializer = TimeStatisticsSerializer(statistics, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = TimeStatisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

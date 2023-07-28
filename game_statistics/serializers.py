'''
Created Date: Tuesday July 25th 2023 2:57:51 pm CEST
Author: Trendon Robinson at <The_Pr0fessor (Rbx), @TPr0fessor (Twitter)>
-----
Last Modified: Tuesday July 25th 2023 2:57:53 pm CEST
Modified By: Trendon Robinson at <The_Pr0fessor (Rbx), @TPr0fessor (Twitter)>
'''
from rest_framework import serializers
from .models import Bow, Purchase, TimeStatistics


class BowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bow
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class TimeStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStatistics
        fields = '__all__'

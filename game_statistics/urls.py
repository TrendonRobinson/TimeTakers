'''
Created Date: Tuesday July 25th 2023 2:56:32 pm CEST
Author: Trendon Robinson at <The_Pr0fessor (Rbx), @TPr0fessor (Twitter)>
-----
Last Modified: Friday July 28th 2023 3:01:07 am CEST
Modified By: Trendon Robinson at <The_Pr0fessor (Rbx), @TPr0fessor (Twitter)>
'''
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('bows/', csrf_exempt(views.BowListView.as_view()), name='bow-list'),
    path('purchases/', csrf_exempt(views.PurchaseView.as_view()),
         name='purchase-list'),
    path('time_statistics/', csrf_exempt(views.TimeStatisticsListView.as_view()),
         name='time-statistics'),
]

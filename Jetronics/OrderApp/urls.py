from django.urls import path
from .views import *


urlpatterns = [
    path('missingorder/',MissingOrderView.as_view()),
    path('allorder/',OrderViews.as_view()),
    path('statuschange/',StatusChange.as_view()),
    path('statuschangemultiply/',StatusChangeMultiply.as_view()),
    path('orderwithphone/',Getorderwithphone.as_view()),
    path('CsvReportView/',CsvReportView.as_view()),
    path('orderwithuser/',Getorderwithuser.as_view()),
    path('missingorderreport/',MissingorderCsvReportView.as_view()),
    path('deletemultiplemissingorder/',DeletMultipleMissingOrder.as_view()),
    path('multipleorders/',allOrder.as_view()),
]
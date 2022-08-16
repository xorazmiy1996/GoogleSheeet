from django.contrib import admin
from django.urls import path
from .views import GoogleSheetView

urlpatterns = [
    path('sheet/',GoogleSheetView.as_view(), name='sheet_url'),


]
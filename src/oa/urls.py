from django.urls import path
from . import views

urlpatterns = [
    path('api/line-chart-data/', views.line_data),
    path('api/bar-chart-data/', views.bar_data),
    path('api/pie-chart-data/', views.pie_data),
    path('api/candlestick-data/', views.candle_data)
]

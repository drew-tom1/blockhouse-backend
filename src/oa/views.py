from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def candle_data(request):
    return Response({
        "data": 
        [
            {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
            {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
        ]
    })

@api_view(['GET'])
def line_data(request):
    print('lol')
    return Response({
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 30, 40]
    })

@api_view(['GET'])
def bar_data(request):
    return Response({
        "labels": ["Product A", "Product B", "Product C"],
        "data": [100, 150, 200]
    })

@api_view(['GET'])
def pie_data(request):
    return Response({
        "labels": ["Red", "Blue", "Yellow"],
        "data": [300, 50, 100]
    })
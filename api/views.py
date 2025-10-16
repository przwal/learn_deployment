from rest_framework import viewsets
from .models import News
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=False, methods=['get'])
    def convert_date(self, request):
        # get date from query params, e.g., /api/news/convert_date/?date=2025-10-16
        date_str = request.query_params.get('date')

        splitted_date = date_str.split('-')
        new_year = int(splitted_date[0]) + 57
        new_month = int(splitted_date[1]) - 4
        new_day = abs(int(splitted_date[2])+12)

        print(new_year,new_month,new_day)
        # here you can later do conversion, for now return 0
        converted_date = f"{new_year}-{new_month}-{new_day}"
        return Response({"original_date": date_str, "converted_date": converted_date})


from rest_framework.pagination import PageNumberPagination

class Mypagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'pg'
    page_size_query_param = 'records'
    # max_page_size = 2
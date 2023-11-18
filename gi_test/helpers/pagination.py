from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from gi_test.helpers.response import ResponseInfo


class RestPagination(PageNumberPagination):
    
    page_size = 25
    page_size_query_param = 'limit'
    
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(RestPagination, self).__init__(**kwargs)


    def get_paginated_response(self, data):
        
        
        data = {
            'links': {
                'next': "" if self.get_next_link() is None else self.get_next_link().split('/api')[1],
                'previous': "" if self.get_previous_link() is None else self.get_previous_link().split('/api')[1]
            },
            'count': self.page.paginator.count,
            'results': data
        }
        
        self.response_format['status_code'] = status.HTTP_200_OK
        self.response_format["data"] = data
        self.response_format["status"] = True
        
        
        return Response(self.response_format, status=status.HTTP_200_OK)
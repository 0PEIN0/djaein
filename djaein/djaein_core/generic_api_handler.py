from rest_framework import status
from rest_framework.response import Response


class GenericApiHandler(object):

    def check_permission(self,
                         method_name,
                         user):
        return True

    def get_paginated_data(self,
                           request,
                           qs):
        return qs, False, qs.count(), {}

    def ok(self,
           data,
           request,
           serializer=None,
           is_listing=False):
        total_element_count = None
        has_next = None
        summary = None
        if is_listing is True:
            total_element_count = 0
            has_next = False
            try:
                data, has_next, total_element_count, summary = self.get_paginated_data(
                    request=request, qs=data)
            except Exception as ex:
                return self.bad(data={'error_code': 'core_generic_api_handler_1', 'extra': str(ex)})
        if serializer is not None:
            serializer = serializer(
                data, many=is_listing, context={'request': request})
            data = serializer.data
        return Response({'data': data,
                         'summary': summary,
                         'total_element_count': total_element_count,
                         'has_next': has_next}, status=status.HTTP_200_OK)

    def bad(self,
            data,
            request):
        return Response({'data': data,
                         'summary': None,
                         'total_element_count': None,
                         'has_next': None}, status=status.HTTP_400_BAD_REQUEST)

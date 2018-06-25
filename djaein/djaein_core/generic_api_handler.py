from rest_framework import status
from rest_framework.response import Response


class GenericApiHandler(object):

    def check_permission(self,
                         method_name,
                         user):
        return True

    def check_serializer(self,
                         request,
                         serializer_class,
                         partial=False,
                         many=False):
        serializer = serializer_class(
            data=request.data, partial=partial, many=many)
        if serializer.is_valid() is False:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST), None
        return None, serializer.validated_data

    def get_paginated_data(self,
                           request,
                           qs):
        summary_obj = {}
        total_element_count = qs.count()
        page_id = request.GET.get('page', None)
        number_of_page_items = request.GET.get(
            'page_size', None)
        if hasattr(qs, 'count') is False:
            return qs, False, total_element_count, summary_obj
        try:
            page_id = int(page_id)
            number_of_page_items = int(number_of_page_items)
        except Exception as ex:
            return qs, False, total_element_count, summary_obj
        return qs, False, total_element_count, {}

    def ok(self,
           data,
           request,
           serializer=None,
           is_listing=False,
           many=False,
           status_code=status.HTTP_200_OK):
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
                data, many=many, context={'request': request})
            data = serializer.data
        return Response({'data': data,
                         'summary': summary,
                         'total_element_count': total_element_count,
                         'has_next': has_next}, status=status_code)

    def created(self,
                data,
                request,
                serializer=None,
                many=False):
        return self.ok(data=data,
                       request=request,
                       serializer=serializer,
                       is_listing=False,
                       many=many,
                       status=status.HTTP_201_CREATED)

    def bad(self,
            data,
            request):
        return Response({'data': data,
                         'summary': None,
                         'total_element_count': None,
                         'has_next': None}, status=status.HTTP_400_BAD_REQUEST)

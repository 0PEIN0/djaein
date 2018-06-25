import sys

from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .generic_api_handler import GenericApiHandler


class BaseApiView(object):

    HANDLER = GenericApiHandler()
    OUTPUT_SERIALIZER = None
    MODEL_CLASS = None
    ORDER_BY = 'id'

    class Meta:
        abstract = True


class BaseListCreateAPIView(BaseApiView, ListCreateAPIView):

    def get_queryset(self,
                     user):
        return MODEL_CLASS.objects.all().order_by(ORDER_BY)

    def get(self,
            request):
        user = request.user
        handler.check_permission(method_name=sys._getframe().f_code.co_name,
                                 user=user)
        data = self.get_queryset(
            user=user)
        if hasattr(self, 'custom_get'):
            data = self.custom_get(data=data)
        return HANDLER.ok(data=data,
                          serializer=OUTPUT_SERIALIZER,
                          request=request,
                          is_listing=True)

    class Meta:
        abstract = True


class BaseRetrieveUpdateDestroyAPIView(BaseApiView, RetrieveUpdateDestroyAPIView):

    class Meta:
        abstract = True

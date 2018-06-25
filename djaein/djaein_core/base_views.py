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
        return self.MODEL_CLASS.objects.all().order_by(self.ORDER_BY)

    def get(self,
            request):
        print(44)
        user = request.user
        self.HANDLER.check_permission(method_name=sys._getframe().f_code.co_name,
                                      user=user)
        data = self.get_queryset(
            user=user)
        if hasattr(self, 'custom_get'):
            data = self.custom_get(data=data)
        return self.HANDLER.ok(data=data,
                               serializer=self.OUTPUT_SERIALIZER,
                               request=request,
                               is_listing=True)

    class Meta:
        abstract = True


class BaseRetrieveUpdateDestroyAPIView(BaseApiView, RetrieveUpdateDestroyAPIView):

    class Meta:
        abstract = True

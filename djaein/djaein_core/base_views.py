import sys

from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .generic_api_handler import GenericApiHandler


class BaseApiView(object):

    HANDLER = GenericApiHandler()
    OUTPUT_SERIALIZER = None
    MODEL_CLASS = None
    BULK_CREATE = False
    PAYLOAD_SERIALIZER = None
    ORDER_BY = 'id'

    class Meta:
        abstract = True


class BaseListCreateAPIView(BaseApiView, ListCreateAPIView):

    def get_queryset(self,
                     user):
        return self.MODEL_CLASS.objects.all().order_by(self.ORDER_BY)

    def get(self,
            request):
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
                               is_listing=True,
                               many=True)

    def post(self,
             request):
        user = request.user
        self.HANDLER.check_permission(method_name=sys._getframe().f_code.co_name,
                                      user=user)
        response, data = self.HANDLER.check_serializer(request=request)
        if response:
            return response
        if hasattr(self, 'custom_post'):
            data = self.custom_post(data=data)
        if self.BULK_CREATE is True:
            response = []
            for item in data:
                response.append(self.MODEL_CLASS.objects.create(**item))
        else:
            response = self.MODEL_CLASS.objects.create(**data)
        return self.HANDLER.created(data=response,
                                    serializer=self.OUTPUT_SERIALIZER,
                                    request=request,
                                    many=self.BULK_CREATE)

    class Meta:
        abstract = True


class BaseRetrieveUpdateDestroyAPIView(BaseApiView, RetrieveUpdateDestroyAPIView):

    class Meta:
        abstract = True

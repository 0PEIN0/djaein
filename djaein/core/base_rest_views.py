from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .generic_api_view_handler import GenericApiViewHandler


class BaseListCreateAPIView(GenericApiViewHandler, ListCreateAPIView):
    pass


class BaseRetrieveUpdateDestroyAPIView(GenericApiViewHandler, RetrieveUpdateDestroyAPIView):
    pass

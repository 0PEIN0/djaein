from djaein_core import BaseRetrieveUpdateDestroyAPIView

from ..models import ToDo


class ToDoFetchUpdateDelete(BaseRetrieveUpdateDestroyAPIView):

    OUTPUT_SERIALIZER = None
    MODEL_CLASS = ToDo
    ORDER_BY = '-date_created'

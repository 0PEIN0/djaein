from djaein_core import BaseListCreateAPIView

from ..models import ToDo
from ..serializers import ToDoOutput


class ToDoListCreate(BaseListCreateAPIView):

    OUTPUT_SERIALIZER = ToDoOutput
    MODEL_CLASS = ToDo
    ORDER_BY = '-date_created'

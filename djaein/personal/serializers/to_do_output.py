from djaein_core import BaseModelSerializer

from ..models import ToDo


class ToDoOutput(BaseModelSerializer):

    class Meta:
        model = ToDo
        fields = ('uuid',
                  'task_name',
                  'is_completed',
                  'date_created',
                  'date_updated',)

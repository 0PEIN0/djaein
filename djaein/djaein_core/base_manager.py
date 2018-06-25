from django.db import models

from .exceptions import DatabaseGetException


class BaseManager(models.Manager):

    def filter_active(self, *args, **kwargs):
        return self.filter(*args,
                           **kwargs,
                           is_active=True)

    def get_by_uuid(self,
                    uuid):
        try:
            model_instance = self.get(uuid=uuid)
        except Exception as ex:
            raise DatabaseGetException(code='core_model_manager_base_1')
        return model_instance

    class Meta:
        abstract = True

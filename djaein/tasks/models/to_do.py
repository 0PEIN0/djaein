from django.db import models

from core import BaseManager, BaseModel


class ToDoManager(BaseManager):
    pass


class ToDo(BaseModel):

    task_name = models.CharField(
        verbose_name='Task Name',
        help_text='Detailed task name.',
        max_length=128,
    )
    is_completed = models.BooleanField(
        verbose_name='Completed',
        default=False,
        help_text='Completed or not.'
    )

    def __str__(self):
        return str(self.task_name)

    objects = ToDoManager()

    class Meta:
        verbose_name = 'To Do'
        verbose_name_plural = 'To Dos'
        db_table = 'tasks_to_dos'

from django.contrib import admin


class ToDoAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uuid',
                    'task_name',
                    'is_completed',)
    search_fields = ('id',
                     'uuid',
                     'task_name',
                     'is_completed',)
    readonly_fields = ('date_created',
                       'date_updated',
                       'uuid',
                       'id',)

from django.conf.urls import url

from personal import views

urlpatterns = [
    url(r'^to-do/$',
        views.ToDoListCreate.as_view()),
    url(r'^to-do/(?P<to_do_uuid>[0-9a-f-]+)/$',
        views.ToDoFetchUpdateDelete.as_view()),
]

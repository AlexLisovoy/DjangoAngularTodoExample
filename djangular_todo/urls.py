from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('todo.urls', 'todo')),
]

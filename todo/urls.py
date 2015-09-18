from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import TaskViewSet


task_router = routers.DefaultRouter()
task_router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='todo/index.html'),
        name='index_page'),
    url(r'', include(task_router.urls)),
]

from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


class IndexPageTestCase(TestCase):

    def test_index_page_success(self):
        resp = self.client.get(reverse('todo:index_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Todos', count=1)


class ApiTests(APITestCase):

    def test_get_tasks(self):
        task_1 = Task.objects.create(name='task #1')
        task_2 = Task.objects.create(name='task #2')
        url = reverse('todo:task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [TaskSerializer(task_1).data,
                                         TaskSerializer(task_2).data])

    def test_create_task(self):
        url = reverse('todo:task-list')
        data = {'name': 'test task'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.get()
        self.assertEqual(task.name, 'test task')
        self.assertFalse(task.is_complete)

    def test_retrive_task(self):
        task = Task.objects.create(name='dummy task')
        url = reverse('todo:task-detail', kwargs={'pk': task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TaskSerializer(task).data)

    def test_patch_task(self):
        task = Task.objects.create(name='dummy task')
        url = reverse('todo:task-detail', kwargs={'pk': task.id})
        response = self.client.patch(url, {'is_complete': True}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Task.objects.get(name='dummy task').is_complete)

    def test_update_task(self):
        task = Task.objects.create(name='dummy task')
        url = reverse('todo:task-detail', kwargs={'pk': task.id})
        response = self.client.put(url, {'name': 'foo', 'is_complete': True},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_task = Task.objects.get(id=task.id)
        self.assertTrue(updated_task.is_complete)
        self.assertEquals('foo', updated_task.name)

    def test_remove_task(self):
        task = Task.objects.create(name='dummy task')
        url = reverse('todo:task-detail', kwargs={'pk': task.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(0, Task.objects.all().count())

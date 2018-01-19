from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CgroupTests(APITestCase):
    def setUp(self):
        self.url = reverse('cgroup-modify', kwargs={'name': 'unittestgroup'})

    def test_add_cgroup(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_cgroup(self):
        self.client.post(self.url)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PidTest(APITestCase):
    def setUp(self):
        self.url = reverse('pid-list', kwargs={'name': 'unittestgroup'})

    def test_list_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)

    def test_add_pid(self):
        url = reverse('pid-modify', kwargs={'name': 'unittestgroup', 'pid': 1})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), 1)

    def test_delete_pid(self):
        url = reverse('pid-modify', kwargs={'name': 'unittestgroup', 'pid': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url)
        self.assertEqual(len(response.json()), 0)

    def test_invalid_pid(self):
        url = reverse('pid-modify', kwargs={'name': 'unittestgroup', 'pid': 10101010})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

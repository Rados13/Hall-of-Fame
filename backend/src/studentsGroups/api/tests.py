import json

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from groups.models import Group
from studentsGroups.models import StudentGroups
User = get_user_model()


class StudentGroupsAPITestCase(APITestCase):

    def setUp(self):
        user_obj = User(email='test@test.com')
        user_obj.set_password("randPassword")
        user_obj.save()
        group = Group()
        group.save()
        student_groups = StudentGroups(user=user_obj)
        student_groups.groups_list.add(group)
        student_groups.save()

    def test_get_groups(self):
        user = User.objects.get()
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.access_token))

        url = reverse('studentsGroups:student')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)

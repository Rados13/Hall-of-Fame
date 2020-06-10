import json

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserAPITestCase(APITestCase):

    def setUp(self):
        user_obj = User(email='test@test.com', first_name="John", last_name="Snow")
        user_obj.set_password("randPassword")
        user_obj.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_student(self):
        student_count = User.objects.filter(is_student=True).count()
        self.assertEqual(student_count, 1)

    def test_none_lecture(self):
        lecture_count = User.objects.filter(is_lecture=True).count()
        self.assertEqual(lecture_count, 0)

    def test_post_new_user(self):
        url = reverse('users:user-create')
        data = {'email': 't@t.com', 'password': 'test', 'first_name': 'Harry', 'last_name': 'Potter'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(first_name='Harry').last_name, 'Potter')

    # Problem with status
    # def test_update_user_info(self):
    #     user = User.objects.get(first_name='John')
    #     self.client.force_authenticate(user=user)
    #
    #     url = reverse('users:user-rud', args=[user.pk])
    #     data = {'is_lecture': True}
    #
    #     response = self.client.patch(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(User.objects.filter(is_lecture=True), 1)

    def test_get_info(self):
        user = User.objects.get(first_name='John')
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.access_token))

        url = reverse('users:user-info')

        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{"is_student":True,"is_lecture":False,"is_admin":False})

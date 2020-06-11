import json

from enrolleds.models import Enrolled
from groups.api.serializers import GroupSerializer
from lectures.models import Lecture
from lectures.serializers import LectureSerializer
from marks.models import Mark
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from groups.models import Group
from lecturesGroups.models import LectureGroups

User = get_user_model()


class GroupAPITestCase(APITestCase):

    def setUp(self):
        lecture = User(email='test@test.com', first_name='John', last_name='Snow', is_student=False, is_lecture=True)
        lecture2 = User(email='t@t.com', first_name='Harry', last_name='Potter', is_student=False, is_lecture=True)
        lecture.set_password("randPassword")
        lecture.save()
        lecture2.save()
        student = User(email='ts@ts.com', first_name='Frodo', last_name='Baggins')
        student2 = User(email='tst@tst.com', first_name='Titus', last_name='Flavius')
        student3 = User(email='py@py.com', first_name='Philip', last_name='Capet')
        student.save()
        student2.save()
        student3.save()

        group = Group(course='python', lectures_list=[Lecture(lecture=lecture)],
                      enrolled_list=[Enrolled(student=student,
                                              marks_list=[Mark(value=5, max_points=10, for_what="exercise", note=""),
                                                          Mark(value=2, max_points=10, for_what="quiz", note="")]),
                                     Enrolled(student=student2,
                                              marks_list=[Mark(value=7, max_points=10, for_what="exercise", note=""),
                                                          Mark(value=10, max_points=10, for_what="quiz", note="")]
                                              )])
        group.save()

    def authorize_client_lecture(self):
        user = User.objects.get(email='test@test.com')
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.access_token))

    def test_get_group_list(self):
        self.authorize_client_lecture()
        url = reverse('groups:create')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)

    def test_post_group_list(self):
        self.authorize_client_lecture()
        url = reverse('groups:create')
        data = {"course": "scala", "date_time": None}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 2)
        self.assertIsNotNone(Group.objects.filter(course='scala')[0].lectures_list[0].lecture)

    def test_get_rud(self):
        self.authorize_client_lecture()
        url = reverse('groups:group-rud', args=[Group.objects.get().pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(json.loads(response.content)['course'], 'python')

    def test_patch_rud(self):
        self.authorize_client_lecture()
        url = reverse('groups:group-rud', args=[Group.objects.get().pk])
        lectures = User.objects.filter(is_lecture=True)
        group = Group.objects.get()
        group.course = 'python2'
        group.lectures_list.append(Lecture(lecture=lectures[1]))
        data = {'group': GroupSerializer(group).data}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(LectureGroups.objects.count(), 2)
        self.assertEqual(Group.objects.all()[0].course, 'python2')

    def authorize_client_student(self, in_group=False):
        index = 0 if in_group else 2
        user = User.objects.filter(is_student=True)[index]
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.access_token))

    def test_post_student_in_group_as_lecture(self):
        self.authorize_client_lecture()
        url = reverse('groups:studentInGroup-rud', args=[Group.objects.get().pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_student_in_group_as_student_already_in_group(self):
        self.authorize_client_student(True)
        url = reverse('groups:studentInGroup-rud', args=[Group.objects.get().pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_student_in_group_as_student(self):
        self.authorize_client_student()
        url = reverse('groups:studentInGroup-rud', args=[Group.objects.get().pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Group.objects.get().enrolled_list), 3)

    def test_mark_all(self):
        self.authorize_client_lecture()
        url = reverse('groups:mark-all', args=[Group.objects.get().pk])
        users = [elem.pk for elem in User.objects.filter(is_student=True)[0:2]]
        data = {'student_marks': {users[0]: {"value": 7, "note": ""}, users[1]: {"value": 5, "note": ""}},
                'mark_name': 'Kolokwium', 'max_points': 10}

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.get().enrolled_list[0].marks_list[2].value, 7)
        self.assertEqual(Group.objects.get().enrolled_list[1].marks_list[2].value, 5)

    def test_stats(self):
        self.authorize_client_lecture()
        url = reverse('groups:stats')
        group = Group.objects.get()

        response = self.client.get(url, {'groups_id[]': [group.pk]})

        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['exercise']['val'], 6)
        self.assertEqual(data['quiz']['val'], 6)
        self.assertEqual(data['total']['val'], 12)

    def test_final_grade(self):
        self.authorize_client_lecture()
        group = Group.objects.get()
        url = reverse('groups:final-grade', args=[group.pk])

        response = self.client.post(url)

        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['enrolled_list'][0]['final_grade'], 2)
        self.assertEqual(data['enrolled_list'][1]['final_grade'], 4.5)


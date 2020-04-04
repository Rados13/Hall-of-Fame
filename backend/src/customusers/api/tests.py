# Something problem with import from apps



from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()
from users.models import CustomUser


class StudentAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testUser', email='test@test.com')
        user_obj.set_password("randPassword")
        user_obj.save()
        student = Student.objects.create(user=user_obj,
                                         name='John',
                                         surname='Snow'
                                         )

        def test_single_user(self):
            user_count = User.objects.count()
            self.asserEqual(user_count, 1)

        def test_single_student(self):
            student_count = Student.objects.count()
            self.asserEqual(student_count, 1)


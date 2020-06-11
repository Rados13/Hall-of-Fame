from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.core.mail import send_mail, send_mass_mail
from .permissions import ReadOnly
from groups.api.permissions import get_user_from_request
from users.models import User


class MailViewAPI(generics.CreateAPIView):
    permission_classes = [ReadOnly]

    def post(self, request, *args, **kwargs):
        user = get_user_from_request(request)
        user_name = user.first_name + "  " + user.last_name + "  <" + user.email + ">"
        users_id = request.data['headers']['to']
        title = request.data['headers']['title']
        message = request.data['headers']['message']
        recipents = self.get_persons_mails(users_id)
        send_mail(title, message, user_name, recipents,fail_silently=False)
        return Response("Sended", status=status.HTTP_200_OK)

    def get_persons_mails(self, to_map):
        users_id = []
        for k, v in to_map.items():
            if v:
                users_id.append(k)
        users = User.objects.filter(pk__in=users_id)
        return [elem.email for elem in users]

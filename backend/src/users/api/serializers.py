from rest_framework import serializers

# from ..models import CustomUser
# from django.contrib.auth import get_user_model
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            # 'uri',
            'pk',
            'first_name',
            'last_name',
        ]


class CustomUserSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    User = User

    class Meta:
        model = User
        fields = [
            # 'uri',
            'pk',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        # write_only_fields = ['password']
        # read_only_fields = ['user']

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(email=email,
                        first_name=first_name,
                        last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request)

    # def validate_name(self, value):
    #     qs = User.objects.filter(name_iexact=value)
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exist():
    #         raise serializers.ValidationError("The name is already used")
    # convert to JSON
    # validations data

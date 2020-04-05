from rest_framework import serializers

# from ..models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    User = get_user_model()

    class Meta:
        model = get_user_model()
        fields = [
            # 'uri',
            'pk',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        # write_only_fields = ['password']
        # read_only_fields = ['user']

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = get_user_model()(username=username,
                                    email=email,
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

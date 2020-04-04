from rest_framework import serializers

# from ..models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    
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
        # read_only_fields = ['user']

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

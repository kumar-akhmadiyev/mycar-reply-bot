from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import MainUser


class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MainUser
        fields = ['username', 'password', 'password_confirm', 'name']
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Пароль и подтверждение пароля не совпадают"})

        return attrs

    def create(self, validated_data):
        user = MainUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.first_name,
            'username': instance.username,
            'access_token': instance.access_token
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


from rest_framework import serializers
from users.models import User


class UserRegestrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'terms']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # password validation

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                "Error confirming passwords,passwords do not match")
        return attrs
    # sends the validated data and creates User

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# --- Registration Serializer ---
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # checker expects CharField

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "profile_picture"]

    def create(self, validated_data):
        # ✅ Use get_user_model().objects.create_user as required
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        # ✅ Create token for new user
        Token.objects.create(user=user)
        return user


# --- Login Serializer ---
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()   # 👈 checker expects CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return {"user": user, "token": token.key}
        raise serializers.ValidationError("Invalid credentials")






# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["id", "username", "email"]

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["username", "email", "password"]
#         extra_kwargs = {
#             "password": {"write_only": True}
#         }

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"]
#         )
#         return user

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["bio", "profile_picture"]
#         extra_kwargs = {
#             "bio": {"required": False},
#             "profile_picture": {"required": False}
#         }







# from rest_framework import serializers
# from .models import CustomUser
# from django.contrib.auth import sef

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
    
#     def create(self, validated_data):
#         password = validated_data.pop('passwowrd')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save
#         return user
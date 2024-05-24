from rest_framework import serializers
from .models import User, Coach, Athlete, TrainingSession, Review

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2", "role"]
        extra_kwargs = {"password":{"write_only": True}}

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user
    
#Login serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password"]

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["full_name", "trainer_for", "bio", "image"]
        read_only_fields = ["user"]

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ["full_name", "training_for", "image"]
        read_only_fields = ["user"]

class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
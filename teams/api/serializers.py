from django.contrib.auth import get_user_model
from rest_framework import serializers

from teams.models import Team

User = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'name'
        ]

    def validate_name(self, value):
        if Team.objects.filter(name=value).exists():
            raise serializers.ValidationError("Team with this name already exists.")
        return value


class UserSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(slug_field='name', queryset=Team.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'team',
        ]

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name should only contain letters.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name should only contain letters.")
        return value

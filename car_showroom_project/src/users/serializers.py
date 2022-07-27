from rest_framework import serializers

from src.users.models import ShowroomUser


class ShowroomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomUser
        fields = [
            "username",
            "email",
            "password",
            "is_customer",
            "is_dealer",
            "is_showroom",
        ]
